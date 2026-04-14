#!/usr/bin/env python3
"""
prompt-inject.py — UserPromptSubmit hook: async QMD context injection

Fires on every user message. Spawns prompt-inject-worker.py in the background
(no latency for user). Results written to .claude/context-inject.md.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

VAULT = Path("F:/My Drive/Obsidian/Codex.os")
INJECT_FILE = VAULT / ".claude/context-inject.md"
WORKER = str(VAULT / ".claude/scripts/prompt-inject-worker.py")
PYTHON_EXE = r"C:\Users\aspor\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe"

SKIP_PHRASES = [
    "AUTOMATED BACKGROUND CHECK",
    "do not treat this as a user message",
    "do not respond conversationally",
    "FRESHDESK",
    "Run: python",
]


def main():
    try:
        raw = sys.stdin.read().strip()
        if not raw:
            return
        data = json.loads(raw)
    except Exception:
        return

    prompt = data.get("prompt", "")
    if not prompt or len(prompt.strip()) < 15:
        try:
            INJECT_FILE.write_text("", encoding="utf-8")
        except Exception:
            pass
        return

    # Skip automated messages
    prompt_check = prompt[:300].upper()
    if any(skip.upper() in prompt_check for skip in SKIP_PHRASES):
        try:
            INJECT_FILE.write_text("", encoding="utf-8")
        except Exception:
            pass
        return

    # Extract keywords — strip filler words so BM25 gets signal, not noise
    STOP = {
        "can", "you", "tell", "me", "about", "the", "a", "an", "and", "or",
        "is", "are", "was", "were", "do", "does", "how", "what", "when",
        "where", "why", "who", "which", "that", "this", "it", "its", "i",
        "in", "on", "at", "for", "to", "of", "with", "have", "has", "had",
        "be", "been", "will", "would", "should", "could", "please", "let",
        "get", "give", "make", "take", "see", "look", "show", "help", "just",
        "also", "up", "out", "so", "if", "but", "not", "my", "we", "our",
        "going", "want", "need", "think", "know", "use", "used", "using",
        "yeah", "yep", "yes", "ok", "okay", "sure", "right", "great", "good",
        "any", "all", "some", "more", "new", "now", "then", "than", "from",
        "into", "like", "as", "by", "its", "vs", "re", "ve", "ll", "d",
    }

    raw_text = re.sub(r"[`*#>|\[\]{}()\"]", " ", prompt[:300])
    words = re.findall(r"[a-zA-Z0-9][\w\-\.]*", raw_text)
    keywords = [w for w in words if w.lower() not in STOP and len(w) > 2]
    query = " ".join(keywords[:5])  # top 5 content words — more than this hurts BM25 recall

    if len(query) < 5:
        return

    # Write query to temp file for worker to read
    query_file = VAULT / ".claude/state/inject-query.txt"
    try:
        query_file.parent.mkdir(parents=True, exist_ok=True)
        query_file.write_text(query, encoding="utf-8")
    except Exception:
        return

    # Spawn worker in background — returns immediately
    try:
        subprocess.Popen(
            [PYTHON_EXE, WORKER],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            cwd=str(VAULT),
        )
    except Exception:
        pass


if __name__ == "__main__":
    main()
