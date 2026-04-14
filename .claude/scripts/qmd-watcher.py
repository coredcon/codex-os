#!/usr/bin/env python3
"""
qmd-watcher.py — Auto-embed watcher for QMD

Watches the Codex.os vault for .md file changes and triggers
`qmd update && qmd embed` after a debounce window.

Run once at session start — loops internally until killed.
"""

import os
import time
import subprocess
import threading
from datetime import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

VAULT = Path(r"F:\My Drive\Obsidian\Codex.os")
LOG_FILE = VAULT / ".claude" / "scripts" / "qmd-watcher.log"

# Directories to ignore (relative to vault root)
SKIP_DIRS = {"07 Archive", ".claude", ".obsidian", ".git", "Templates"}

# Only watch these extensions
WATCH_EXTS = {".md"}

# Debounce — wait this many seconds after last change before running embed
DEBOUNCE_SECONDS = 8


def log(msg: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def run_qmd_update():
    log("Change detected — running qmd update + embed...")
    try:
        result = subprocess.run(
            ["qmd", "update"],
            capture_output=True, text=True, timeout=120,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        if result.returncode == 0:
            log("qmd update OK")
        else:
            log(f"qmd update exit {result.returncode}: {result.stderr.strip()[:200]}")
    except Exception as e:
        log(f"qmd update error: {e}")

    try:
        result = subprocess.run(
            ["qmd", "embed"],
            capture_output=True, text=True, timeout=300,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        if result.returncode == 0:
            log("qmd embed OK")
        else:
            log(f"qmd embed exit {result.returncode}: {result.stderr.strip()[:200]}")
    except Exception as e:
        log(f"qmd embed error: {e}")


def should_skip(path: str) -> bool:
    """Return True if this path should be ignored."""
    p = Path(path)
    # Check extension
    if p.suffix.lower() not in WATCH_EXTS:
        return True
    # Check if any parent folder is in the skip list
    try:
        rel = p.relative_to(VAULT)
        for part in rel.parts[:-1]:  # all dirs, not the filename
            if part in SKIP_DIRS:
                return True
    except ValueError:
        return True
    return False


class VaultHandler(FileSystemEventHandler):
    def __init__(self):
        self._timer: threading.Timer | None = None
        self._lock = threading.Lock()
        self._pending_count = 0

    def _schedule(self):
        """Debounce: reset timer on each event, fire once after quiet period."""
        with self._lock:
            self._pending_count += 1
            if self._timer is not None:
                self._timer.cancel()
            self._timer = threading.Timer(DEBOUNCE_SECONDS, self._fire)
            self._timer.start()

    def _fire(self):
        with self._lock:
            count = self._pending_count
            self._pending_count = 0
            self._timer = None
        log(f"Debounce complete ({count} change(s) batched)")
        run_qmd_update()

    def on_modified(self, event):
        if not event.is_directory and not should_skip(event.src_path):
            self._schedule()

    def on_created(self, event):
        if not event.is_directory and not should_skip(event.src_path):
            self._schedule()

    def on_deleted(self, event):
        if not event.is_directory and not should_skip(event.src_path):
            self._schedule()

    def on_moved(self, event):
        if not event.is_directory and (
            not should_skip(event.src_path) or not should_skip(event.dest_path)
        ):
            self._schedule()


def main():
    log(f"QMD Watcher started — watching {VAULT}")
    log(f"Skipping: {', '.join(sorted(SKIP_DIRS))}")
    log(f"Debounce: {DEBOUNCE_SECONDS}s")

    handler = VaultHandler()
    observer = Observer()
    observer.schedule(handler, str(VAULT), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(30)
            if not observer.is_alive():
                log("Observer died — restarting")
                observer = Observer()
                observer.schedule(handler, str(VAULT), recursive=True)
                observer.start()
    except KeyboardInterrupt:
        log("Shutting down")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
