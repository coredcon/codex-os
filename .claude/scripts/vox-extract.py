#!/usr/bin/env python3
"""
vox-extract.py — Vox Stop Hook: local, zero-cost memory extraction

Reads the session transcript, extracts facts that may not have made it
into WORKING.md, and writes them to .claude/extraction-queue.md for
Vox to promote at next session start.

Runs on every Stop event — deduplication keeps it safe.
No API calls. No LLM. Regex + heuristics only.
"""

import json
import os
import re
import sys
import subprocess
from datetime import datetime
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────────

VAULT = Path("F:/My Drive/Obsidian/Codex.os")
WORKING_MD   = VAULT / ".vox-working.md"
QUEUE_FILE   = VAULT / ".claude/extraction-queue.md"
QMD_STAMP    = VAULT / ".claude/state/qmd-last-reindex.txt"

QUEUE_HEADER = """\
# Vox Extraction Queue
> Auto-extracted from session transcript on each Stop event.
> Vox reviews at session start and promotes to appropriate files, then clears.
> Deduplication is applied — safe to accumulate across multiple sessions.

---

"""

# ─── Hook data ────────────────────────────────────────────────────────────────

hook_data = {}
try:
    raw = sys.stdin.read().strip()
    if raw:
        hook_data = json.loads(raw)
except Exception:
    pass

transcript_path = hook_data.get("transcript_path", "")
today = datetime.now().strftime("%Y-%m-%d")

# ─── Read existing WORKING.md + queue (for dedup) ─────────────────────────────

working_content = ""
try:
    working_content = WORKING_MD.read_text(encoding="utf-8").lower()
except Exception:
    pass

existing_queue = ""
try:
    existing_queue = QUEUE_FILE.read_text(encoding="utf-8")
except Exception:
    pass

# ─── Parse transcript ─────────────────────────────────────────────────────────

if not transcript_path or not os.path.exists(transcript_path):
    # Fallback: find most recent JSONL in project dir
    proj_dir = Path("C:/Users/aspor/.claude/projects/F--My-Drive-Obsidian-Codex-os")
    try:
        candidates = sorted(proj_dir.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
        if candidates:
            transcript_path = str(candidates[0])
    except Exception:
        pass

entries = []
if transcript_path and os.path.exists(transcript_path):
    try:
        with open(transcript_path, encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entries.append(json.loads(line))
                except Exception:
                    pass
    except Exception:
        pass

# ─── Extraction patterns ───────────────────────────────────────────────────────
# Conservative — only match things that are clearly structured facts.
# Better to miss something than to pollute the queue with noise.

PATTERNS = {
    "job_app": [
        r"[Aa]pplied to ([A-Z][^.()\n]{5,80}?)(?:\s*\(|\s*—|\s*\$|\.$|\n|$)",
        r"[Aa]pplication submitted[^\n]*?(?:to|for|at)\s+([A-Z][^.\n]{5,60})",
    ],
    "momentum": [
        r"(?:[Ss]hipped|[Ll]aunched|[Ff]ully operational|[Cc]onfirmed working)[:\s—–]+([^\n.]{10,120})",
        r"([A-Z][^.\n]{10,100}?)\s+(?:shipped|complete|live|operational|confirmed working)[.—]",
    ],
    "open_loop": [
        r"[Oo]pen [Ll]oop[:\s—–]+([^\n.]{10,120})",
        r"[Ss]till (?:needs|pending|deferred)[:\s—–]+([^\n.]{10,120})",
        r"\[ \]\s+([^\n]{10,120})",  # unchecked task
    ],
    "decision": [
        r"[Dd]ecision[:\s—–]+([^\n.]{10,120})",
        r"[Dd]ecided (?:to|on|that)\s+([^\n.]{10,120})",
    ],
    "pressure": [
        r"[Dd]eadline[:\s—–]+([^\n.]{10,80})",
        r"(?:by|due)\s+(\d{4}-\d{2}-\d{2}[^\n.]{0,60})",
    ],
}

extracted = []  # list of (category, text)

for entry in entries:
    if not isinstance(entry, dict):
        continue
    msg = entry.get("message", {})
    if not isinstance(msg, dict):
        continue
    content = msg.get("content", [])
    if not isinstance(content, list):
        continue

    for block in content:
        if not isinstance(block, dict):
            continue

        btype = block.get("type", "")

        # ── Vault file writes (Write or Edit tool calls) ──
        if btype == "tool_use" and block.get("name") in ("Write", "Edit"):
            fp = block.get("input", {}).get("file_path", "")
            if fp:
                fp_norm = fp.replace("\\", "/")
                vault_norm = str(VAULT).replace("\\", "/")
                if vault_norm in fp_norm:
                    rel = fp_norm.replace(vault_norm + "/", "").replace(vault_norm, "")
                    rel = rel.lstrip("/")
                    # Skip system/temp files
                    if not any(skip in rel for skip in [".tmp", "WORKING.md", "extraction-queue", "extraction-log", "snapshots/", "state/qmd"]):
                        extracted.append(("vault_write", rel))

        # ── Assistant text — pattern match ──
        if btype == "text" and entry.get("type") == "assistant":
            text = block.get("text", "")
            for category, patterns in PATTERNS.items():
                for pat in patterns:
                    for m in re.finditer(pat, text):
                        fact = m.group(1).strip().rstrip(".,")
                        # Quality gate: length, real words, and no documentation/code artifacts
                        if not (10 <= len(fact) <= 150):
                            continue
                        if not re.search(r"[a-zA-Z]{3}", fact):
                            continue
                        # Filter out lines that look like code/docs, not facts
                        if any(skip in fact for skip in [" → ", "` →", "→ ", "`[", "[X]", "X`", '" →', '/ by /']):
                            continue
                        if fact.startswith(("→", "`", "#", "//", "/*")):
                            continue
                        extracted.append((category, fact))

# ─── Deduplicate ──────────────────────────────────────────────────────────────

def already_known(text: str) -> bool:
    """Check if this text is already in WORKING.md or the existing queue."""
    key = text.lower()[:50]
    return key in working_content or key in existing_queue.lower()

seen_keys: set[str] = set()
new_items = []
for cat, text in extracted:
    key = f"{cat}|{text.lower()[:60]}"
    if key in seen_keys:
        continue
    seen_keys.add(key)
    if not already_known(text):
        new_items.append((cat, text))

# ─── Write extraction queue ───────────────────────────────────────────────────

if new_items:
    if not existing_queue.strip():
        content = QUEUE_HEADER
    else:
        content = existing_queue.rstrip() + "\n"

    for cat, text in new_items:
        line = f"{today} | {cat} | {text}\n"
        content += line

    try:
        QUEUE_FILE.parent.mkdir(parents=True, exist_ok=True)
        QUEUE_FILE.write_text(content, encoding="utf-8")
    except Exception as e:
        pass  # Silent fail — never break the session

# ─── QMD reindex (throttled — at most once per 45 min) ───────────────────────

try:
    last_reindex = 0.0
    if QMD_STAMP.exists():
        last_reindex = float(QMD_STAMP.read_text().strip())
    now = datetime.now().timestamp()

    if now - last_reindex > 2700:  # 45 minutes
        subprocess.Popen(
            "qmd update",
            cwd=str(VAULT),
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        QMD_STAMP.parent.mkdir(parents=True, exist_ok=True)
        QMD_STAMP.write_text(str(now))
except Exception:
    pass
