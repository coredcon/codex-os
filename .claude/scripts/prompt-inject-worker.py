#!/usr/bin/env python3
"""
prompt-inject-worker.py — background QMD search worker

Reads query from .claude/state/inject-query.txt, runs qmd search,
writes formatted results to .claude/context-inject.md.

Spawned by prompt-inject.py — never run directly.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

VAULT = Path("F:/My Drive/Obsidian/Codex.os")
INJECT_FILE = VAULT / ".claude/context-inject.md"
QUERY_FILE = VAULT / ".claude/state/inject-query.txt"
BASH = r"C:\Program Files\Git\usr\bin\bash.exe"
VAULT_BASH = "/f/My Drive/Obsidian/Codex.os"

MIN_SCORE = 0.45
MAX_RESULTS = 3
MAX_SNIPPET = 280


def main():
    # Read query
    try:
        query = QUERY_FILE.read_text(encoding="utf-8").strip()
    except Exception:
        return

    if not query or len(query) < 5:
        return

    # Escape query for bash single-quote safety
    query_safe = query.replace("'", "'\\''")
    bash_cmd = (
        f"cd '{VAULT_BASH}' && "
        f"qmd search -n {MAX_RESULTS} --json --min-score {MIN_SCORE} '{query_safe}'"
    )

    # Run qmd search via Git Bash (qmd is in bash PATH but not Windows subprocess PATH)
    try:
        result = subprocess.run(
            [BASH, "-c", bash_cmd],
            capture_output=True, text=True, timeout=8
        )
    except Exception:
        INJECT_FILE.write_text("", encoding="utf-8")
        return

    if result.returncode != 0 or not result.stdout.strip():
        INJECT_FILE.write_text("", encoding="utf-8")
        return

    try:
        hits = json.loads(result.stdout)
    except Exception:
        INJECT_FILE.write_text("", encoding="utf-8")
        return

    if not hits:
        INJECT_FILE.write_text("", encoding="utf-8")
        return

    # Format output
    ts = datetime.now().strftime("%H:%M:%S")
    lines = ["<!-- context-inject " + ts + " -->", ""]

    for h in hits:
        path = h.get("file", "")
        path = path.replace("qmd://codex/", "").replace("qmd://", "")
        title = h.get("title", path)
        score = h.get("score", 0)
        snippet = h.get("snippet", "")

        # Clean snippet — strip @@ diff markers
        if "@@" in snippet:
            snippet = snippet.split("@@")[-1].strip()
        snippet = snippet[:MAX_SNIPPET].strip()

        pct = str(int(score * 100))
        lines.append("**" + title + "** (" + pct + "% — `" + path + "`)")
        if snippet:
            lines.append(snippet)
        lines.append("")

    INJECT_FILE.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
