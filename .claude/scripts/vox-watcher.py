#!/usr/bin/env python3
"""
vox-watcher.py — Ambient context watcher for Vox

Primary: Spotify Web API (if spotify-token.json exists)
Fallback: Windows process window title scraping
Also: active foreground window via user32.dll

Writes a snapshot to .claude/ambient-context.md every 60s.
Run once at session start — loops internally until killed.
"""

import subprocess
import ctypes
import ctypes.wintypes
import json
import os
import time
import urllib.request
import urllib.parse
from datetime import datetime

VAULT = "F:/My Drive/Obsidian/Codex.os"
OUTPUT = os.path.join(VAULT, ".claude/ambient-context.md")
TOKEN_FILE = os.path.join(VAULT, ".claude/scripts/spotify-token.json")
CLIENT_ID = "fcd51263339842ffa8a6e6e2beb1847a"
POLL_INTERVAL = 60  # seconds

# Browser apps: show app name but NOT tab title
BROWSER_APPS = {"firefox", "chrome", "msedge", "brave", "opera", "arc"}
# Vivaldi: show title unless it's a private window
VIVALDI_PRIVATE_MARKER = "private"

# Media apps and how to parse their window titles
# Format: process_name -> (display_name, title_format)
# title_format: "artist - song" | "passthrough" | None
MEDIA_APPS = {
    "spotify": ("Spotify", "artist - song"),
    "vlc":     ("VLC",     "passthrough"),   # VLC shows filename or stream
    "foobar2000": ("foobar2000", "passthrough"),
    "musicbee": ("MusicBee", "passthrough"),
    "groove":   ("Groove Music", "passthrough"),
}


# --- Spotify Web API ---

def load_tokens():
    if not os.path.exists(TOKEN_FILE):
        return None
    with open(TOKEN_FILE) as f:
        return json.load(f)

def save_tokens(data):
    with open(TOKEN_FILE, "w") as f:
        json.dump(data, f, indent=2)

def refresh_access_token(refresh_token):
    data = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
    }).encode()
    req = urllib.request.Request(
        "https://accounts.spotify.com/api/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=8) as resp:
        return json.loads(resp.read())

def get_spotify_api_playing():
    """Use Spotify Web API for now-playing. Returns media dict or None."""
    tokens = load_tokens()
    if not tokens:
        return None
    try:
        access_token = tokens.get("access_token", "")
        req = urllib.request.Request(
            "https://api.spotify.com/v1/me/player/currently-playing",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                if resp.status == 204:
                    return None  # nothing playing
                data = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 401:
                # Token expired — refresh
                new_tokens = refresh_access_token(tokens["refresh_token"])
                tokens["access_token"] = new_tokens["access_token"]
                if "refresh_token" in new_tokens:
                    tokens["refresh_token"] = new_tokens["refresh_token"]
                tokens["saved_at"] = datetime.now().isoformat()
                save_tokens(tokens)
                req = urllib.request.Request(
                    "https://api.spotify.com/v1/me/player/currently-playing",
                    headers={"Authorization": f"Bearer {tokens['access_token']}"},
                )
                with urllib.request.urlopen(req, timeout=8) as resp:
                    if resp.status == 204:
                        return None
                    data = json.loads(resp.read())
            else:
                return None

        if not data or not data.get("item"):
            return None

        item = data["item"]
        artists = ", ".join(a["name"] for a in item.get("artists", []))
        title = item.get("name", "")
        album = item.get("album", {}).get("name", "")
        is_playing = data.get("is_playing", False)
        progress_ms = data.get("progress_ms", 0)
        duration_ms = item.get("duration_ms", 0)

        return {
            "artist": artists,
            "title": title,
            "album": album,
            "app": "Spotify",
            "is_playing": is_playing,
            "progress_ms": progress_ms,
            "duration_ms": duration_ms,
            "source": "api",
        }
    except Exception:
        return None


# --- Window title fallback ---

def get_all_windows():
    """Get all process names + window titles via PowerShell ps1 file."""
    ps1 = os.path.join(VAULT, ".claude/scripts/get-windows.ps1")
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-File", ps1],
            capture_output=True, text=True, timeout=10,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        windows = {}
        for line in result.stdout.strip().splitlines():
            if "|" in line:
                proc, title = line.split("|", 1)
                windows[proc.strip().lower()] = title.strip()
        return windows
    except Exception:
        return {}


def get_foreground_app():
    """Get the currently focused app via user32."""
    try:
        user32 = ctypes.windll.user32
        hwnd = user32.GetForegroundWindow()
        # Get process name
        pid = ctypes.wintypes.DWORD()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        # Get title
        buf = ctypes.create_unicode_buffer(512)
        user32.GetWindowTextW(hwnd, buf, 512)
        title = buf.value.strip()
        # Get process name via kernel32
        kernel32 = ctypes.windll.kernel32
        PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid.value)
        if handle:
            exe_buf = ctypes.create_unicode_buffer(260)
            size = ctypes.wintypes.DWORD(260)
            if ctypes.windll.kernel32.QueryFullProcessImageNameW(handle, 0, exe_buf, ctypes.byref(size)):
                exe = os.path.basename(exe_buf.value).replace(".exe", "").lower()
                kernel32.CloseHandle(handle)
                return {"app": exe, "title": title}
            kernel32.CloseHandle(handle)
        return {"app": "unknown", "title": title}
    except Exception:
        return None


def get_now_playing(windows):
    """Check known media app window titles for now-playing info."""
    for proc, (display, fmt) in MEDIA_APPS.items():
        if proc in windows:
            title = windows[proc]
            if not title or title.lower() == proc:
                # App open but nothing playing (Spotify shows just "Spotify" when idle)
                continue
            if fmt == "artist - song" and " - " in title:
                parts = title.split(" - ", 1)
                return {
                    "artist": parts[0].strip(),
                    "title": parts[1].strip(),
                    "app": display,
                    "raw": title,
                }
            elif fmt == "passthrough":
                return {"artist": "", "title": title, "app": display, "raw": title}
    return None


def fmt_duration(ms):
    s = ms // 1000
    return f"{s // 60}:{s % 60:02d}"

def write_context(media, foreground, windows):
    now = datetime.now()
    lines = [
        "# Vox Ambient Context",
        f"> Updated: {now.strftime('%Y-%m-%d %H:%M')} ET",
        "",
    ]

    if media:
        artist_part = f"**{media['artist']}** — " if media.get("artist") else ""
        status = "▶" if media.get("is_playing", True) else "⏸"
        lines += [
            "## Now Playing",
            f"- {status} {artist_part}{media['title']}",
        ]
        if media.get("album"):
            lines.append(f"- Album: {media['album']}")
        if media.get("duration_ms"):
            lines.append(f"- Progress: {fmt_duration(media['progress_ms'])} / {fmt_duration(media['duration_ms'])}")
        source = media.get("source", "window")
        lines.append(f"- Via: {media['app']} ({'API' if source == 'api' else 'window title'})")
        lines.append("")
    else:
        lines += ["## Now Playing", "- (nothing detected)", ""]

    if foreground:
        app = foreground.get("app", "")
        title = foreground.get("title", "")
        if app in BROWSER_APPS:
            lines += ["## Active App", f"- {app} (browsing)", ""]
        elif app == "vivaldi":
            if VIVALDI_PRIVATE_MARKER in title.lower():
                lines += ["## Active App", "- vivaldi (private)", ""]
            elif title:
                lines += ["## Active App", f"- vivaldi: {title}", ""]
            else:
                lines += ["## Active App", "- vivaldi", ""]
        elif title:
            lines += ["## Active App", f"- {app}: {title}", ""]
        else:
            lines += ["## Active App", f"- {app}", ""]

    # Surface other notable open apps (BambuStudio, Obsidian, etc.)
    notable = []
    notable_map = {
        "bambu-studio": "BambuStudio",
        "bambu_studio": "BambuStudio",
        "prusaslicer": "PrusaSlicer",
        "orca": "OrcaSlicer",
    }
    for proc, label in notable_map.items():
        if proc in windows and windows[proc]:
            notable.append(f"{label}: {windows[proc]}")
    if notable:
        lines += ["## Also Open"] + [f"- {n}" for n in notable] + [""]

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    api_available = os.path.exists(TOKEN_FILE)
    try:
        print(f"Vox Watcher started - polling every {POLL_INTERVAL}s -> {OUTPUT}")
        print(f"Spotify: {'API mode' if api_available else 'window title fallback'}")
    except Exception:
        pass
    while True:
        try:
            windows = get_all_windows()
            # Try API first, fall back to window title
            media = get_spotify_api_playing() if api_available else None
            if media is None:
                media = get_now_playing(windows)
            foreground = get_foreground_app()
            write_context(media, foreground, windows)
        except Exception as e:
            try:
                with open(OUTPUT, "a") as f:
                    f.write(f"\n> Watcher error: {e}\n")
            except Exception:
                pass
        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
