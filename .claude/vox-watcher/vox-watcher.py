#!/usr/bin/env python3
"""
VoxWatcher — Vault file watcher for Codex.os
Monitors watched directories, logs changes to .claude/pending-reflection.md,
and triggers QMD re-index. Runs silently in the Windows system tray.

Install dependencies: pip install watchdog pystray pillow

Usage: python vox-watcher.py
       (Add to Windows startup via Task Scheduler or shell:startup)
"""

import json
import os
import subprocess
import sys
import threading
from datetime import datetime
from pathlib import Path

import pystray
from pystray import Menu, MenuItem as item
from PIL import Image, ImageDraw
from watchdog.observers import Observer
from watchdog.events import (
    FileSystemEventHandler,
    FileCreatedEvent,
    FileModifiedEvent,
    FileDeletedEvent,
    FileMovedEvent,
)
import tkinter as tk
from tkinter import filedialog

# ── Paths ──────────────────────────────────────────────────────────────────────
# Update VAULT_ROOT to your vault location
VAULT_ROOT = Path("[YOUR_VAULT_PATH]")
CONFIG_FILE = VAULT_ROOT / ".claude" / "vox-watcher" / "config.json"
REFLECTION_FILE = VAULT_ROOT / ".claude" / "pending-reflection.md"

# ── Default config ─────────────────────────────────────────────────────────────
DEFAULT_CONFIG = {
    "watched_dirs": [str(VAULT_ROOT)],
    "ignore_patterns": [".git", ".obsidian", "__pycache__", "vox-watcher"],
    "ignore_extensions": [".tmp", ".bak", ".swp"],
    "qmd_enabled": True,
    "paused": False,
    "debounce_seconds": 5,
}


# ── Config helpers ─────────────────────────────────────────────────────────────
def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            data = json.load(f)
        for k, v in DEFAULT_CONFIG.items():
            data.setdefault(k, v)
        return data
    return DEFAULT_CONFIG.copy()


def save_config(config):
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


# ── Reflection log ─────────────────────────────────────────────────────────────
def log_change(path, change_type):
    REFLECTION_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not REFLECTION_FILE.exists() or REFLECTION_FILE.stat().st_size == 0:
        with open(REFLECTION_FILE, "w") as f:
            f.write("# Pending Reflection Queue\n")
            f.write("> Files changed since last Vox session.\n")
            f.write("> Vox processes and clears this at session start.\n\n")

    with open(REFLECTION_FILE, "a") as f:
        f.write(f"- [{timestamp}] `{change_type}` — `{path}`\n")


# ── File event handler ─────────────────────────────────────────────────────────
class VaultEventHandler(FileSystemEventHandler):
    def __init__(self, app):
        self.app = app
        self._debounce_timer = None
        self._pending_changes = []
        self._lock = threading.Lock()

    def should_ignore(self, path):
        path_str = str(path)
        config = self.app.config
        for pattern in config.get("ignore_patterns", []):
            if pattern in path_str:
                return True
        for ext in config.get("ignore_extensions", []):
            if path_str.endswith(ext):
                return True
        return False

    def on_any_event(self, event):
        if self.app.config.get("paused"):
            return
        if event.is_directory:
            return
        if self.should_ignore(event.src_path):
            return

        if isinstance(event, FileCreatedEvent):
            change_type = "created"
        elif isinstance(event, FileModifiedEvent):
            change_type = "modified"
        elif isinstance(event, FileDeletedEvent):
            change_type = "deleted"
        elif isinstance(event, FileMovedEvent):
            change_type = "moved"
        else:
            return

        with self._lock:
            self._pending_changes.append((event.src_path, change_type))
            if self._debounce_timer:
                self._debounce_timer.cancel()
            debounce = self.app.config.get("debounce_seconds", 5)
            self._debounce_timer = threading.Timer(debounce, self._flush)
            self._debounce_timer.start()

    def _flush(self):
        with self._lock:
            changes = list(self._pending_changes)
            self._pending_changes.clear()
            self._debounce_timer = None

        for path, change_type in changes:
            log_change(path, change_type)

        if changes and self.app.config.get("qmd_enabled"):
            self.app.run_qmd_update()


# ── Icon builder ───────────────────────────────────────────────────────────────
def make_icon(state="active"):
    size = 64
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    colors = {
        "active": (70, 130, 180, 255),
        "paused": (140, 140, 140, 255),
        "error": (200, 60, 60, 255),
    }
    fill = colors.get(state, colors["active"])
    draw.ellipse([4, 4, 60, 60], fill=fill)
    draw.ellipse([20, 20, 44, 44], fill=(255, 255, 255, 220))
    draw.ellipse([27, 27, 37, 37], fill=(20, 20, 60, 255))
    return img


# ── Main app ───────────────────────────────────────────────────────────────────
class VoxWatcherApp:
    def __init__(self):
        self.config = load_config()
        self.observer = None
        self.tray = None
        self._handler = None

    def _start_observer(self):
        if self.observer and self.observer.is_alive():
            self.observer.stop()
            self.observer.join()

        self._handler = VaultEventHandler(self)
        self.observer = Observer()
        for d in self.config.get("watched_dirs", []):
            if os.path.isdir(d):
                self.observer.schedule(self._handler, d, recursive=True)

        if not self.config.get("paused"):
            self.observer.start()

    def run_qmd_update(self):
        try:
            subprocess.Popen(
                ["qmd", "update"],
                creationflags=subprocess.CREATE_NO_WINDOW,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except Exception:
            pass

    def add_directory(self, icon=None, item=None):
        def _pick():
            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            directory = filedialog.askdirectory(title="Add Watch Directory")
            root.destroy()
            if directory and directory not in self.config["watched_dirs"]:
                self.config["watched_dirs"].append(directory)
                save_config(self.config)
                self._start_observer()
                self._refresh_menu()
        threading.Thread(target=_pick, daemon=True).start()

    def _make_remove_fn(self, directory):
        def _remove(icon=None, item=None):
            if directory in self.config["watched_dirs"]:
                self.config["watched_dirs"].remove(directory)
                save_config(self.config)
                self._start_observer()
                self._refresh_menu()
        return _remove

    def toggle_pause(self, icon=None, item=None):
        self.config["paused"] = not self.config["paused"]
        save_config(self.config)
        if self.config["paused"]:
            if self.observer and self.observer.is_alive():
                self.observer.stop()
            self.tray.icon = make_icon("paused")
            self.tray.title = "VoxWatcher — Paused"
        else:
            self._start_observer()
            self.tray.icon = make_icon("active")
            self.tray.title = "VoxWatcher — Active"
        self._refresh_menu()

    def toggle_qmd(self, icon=None, item=None):
        self.config["qmd_enabled"] = not self.config["qmd_enabled"]
        save_config(self.config)
        self._refresh_menu()

    def clear_queue(self, icon=None, item=None):
        if REFLECTION_FILE.exists():
            REFLECTION_FILE.unlink()

    def exit_app(self, icon=None, item=None):
        if self.observer and self.observer.is_alive():
            self.observer.stop()
        self.tray.stop()

    def _build_menu(self):
        paused = self.config.get("paused", False)
        qmd_on = self.config.get("qmd_enabled", True)
        watched = self.config.get("watched_dirs", [])

        remove_items = [
            item(f"{Path(d).name}  ({d})", self._make_remove_fn(d))
            for d in watched
        ] or [item("(none)", lambda i, m: None, enabled=False)]

        return Menu(
            item("VoxWatcher", lambda i, m: None, enabled=False),
            Menu.SEPARATOR,
            item("Add Directory...", self.add_directory),
            item("Remove Directory", Menu(*remove_items)),
            Menu.SEPARATOR,
            item("Resume Watching" if paused else "Pause Watching", self.toggle_pause),
            item(f"QMD Re-index: {'ON ✓' if qmd_on else 'OFF'}", self.toggle_qmd),
            item("Clear Reflection Queue", self.clear_queue),
            Menu.SEPARATOR,
            item("Exit", self.exit_app),
        )

    def _refresh_menu(self):
        if self.tray:
            self.tray.menu = self._build_menu()

    def run(self):
        self._start_observer()
        paused = self.config.get("paused", False)
        self.tray = pystray.Icon(
            "VoxWatcher",
            make_icon("paused" if paused else "active"),
            "VoxWatcher — " + ("Paused" if paused else "Active"),
            menu=self._build_menu(),
        )
        self.tray.run()


if __name__ == "__main__":
    app = VoxWatcherApp()
    app.run()
