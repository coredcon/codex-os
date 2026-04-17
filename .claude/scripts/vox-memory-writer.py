#!/usr/bin/env python3
"""
vox-memory-writer.py — Haiku-powered session memory extractor v2

Reads new transcript lines since last Stop, extracts facts/feedback/decisions,
detects contradictions with existing memory, writes memory files.

Sources:
  Primary:       transcript_path from stdin JSON (Stop hook payload)
  Supplementary: .vox-working.md (appended to context if non-empty)

Contradiction resolution:
  Detected contradictions → .claude/pending-contradictions.md
  Vox reads this at session start and asks Corey which fact is correct.

Called by: Stop hook (async) in settings.json
Manual run: python vox-memory-writer.py [--transcript <path>]
"""

import json
import os
import re
import sys
import traceback
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

VAULT             = Path(r"F:\My Drive\Obsidian\Codex.os")
WORKING_MD        = VAULT / ".vox-working.md"
MEMORY_DIR        = Path(r"C:\Users\aspor\.claude\projects\F--My-Drive-Obsidian-Codex-os\memory")
MEMORY_INDEX      = MEMORY_DIR / "MEMORY.md"
ANTHROPIC_ENV     = VAULT / ".claude" / "config" / "anthropic.env"
LOG_FILE          = VAULT / ".claude" / "scripts" / "vox-memory-writer.log"
STATE_DIR         = VAULT / ".claude" / "state"
POSITION_FILE     = STATE_DIR / "memory-writer-positions.json"
CONTRADICTIONS_MD = VAULT / ".claude" / "pending-contradictions.md"

MODEL             = "claude-haiku-4-5-20251001"
MAX_NEW_CHARS     = 12000   # cap on transcript text sent to Haiku
MIN_MEANINGFUL_CHARS = 300  # skip Haiku call if less than this after filtering

# Prefixes that indicate silent/cron prompts — skip these exchanges entirely
SILENT_PROMPT_PREFIXES = (
    "silent freshdesk check",
    "daily dice job search",
    "daily indeed job search",
    "silent check",
)
HEADER_SENTINEL   = "<!-- Vox writes below this line during sessions -->"


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def log(msg: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {msg}\n")
    except Exception:
        pass


# ---------------------------------------------------------------------------
# API key
# ---------------------------------------------------------------------------

def load_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if key:
        return key
    if ANTHROPIC_ENV.exists():
        for line in ANTHROPIC_ENV.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("ANTHROPIC_API_KEY="):
                return line.split("=", 1)[1].strip()
    return ""


# ---------------------------------------------------------------------------
# Transcript reading
# ---------------------------------------------------------------------------

def load_positions() -> dict:
    if POSITION_FILE.exists():
        try:
            return json.loads(POSITION_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def save_position(session_id: str, line_count: int):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    positions = load_positions()
    positions[session_id] = line_count
    # Keep only last 20 sessions to prevent unbounded growth
    if len(positions) > 20:
        oldest = sorted(positions.keys())[:-20]
        for k in oldest:
            del positions[k]
    POSITION_FILE.write_text(json.dumps(positions, indent=2), encoding="utf-8")


def extract_text_from_content(content) -> str:
    """Extract plain text from a message content field (string or list of blocks)."""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", "").strip())
        return "\n".join(p for p in parts if p)
    return ""


def read_new_transcript_lines(transcript_path: str, session_id: str) -> tuple[str, int]:
    """
    Read new user/assistant turns from transcript since last position.
    Returns (formatted_text, total_lines_in_file).
    """
    path = Path(transcript_path)
    if not path.exists():
        log(f"Transcript not found: {transcript_path}")
        return "", 0

    positions = load_positions()
    last_position = positions.get(session_id, 0)

    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    total_lines = len(lines)
    new_lines = lines[last_position:]

    if not new_lines:
        return "", total_lines

    exchanges = []
    skip_next_assistant = False  # skip the assistant reply to a filtered user prompt
    for line in new_lines:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue

        msg = obj.get("message")
        if not msg or not isinstance(msg, dict):
            continue

        role = msg.get("role", "")
        if role not in ("user", "assistant"):
            continue

        content = msg.get("content", "")
        text = extract_text_from_content(content)
        if not text:
            continue

        # Skip very short or purely mechanical lines
        if len(text) < 10:
            continue

        # Filter out known silent/cron prompts and their responses
        if role == "user":
            if text.lower().startswith(SILENT_PROMPT_PREFIXES):
                skip_next_assistant = True
                continue
            else:
                skip_next_assistant = False
        elif role == "assistant" and skip_next_assistant:
            skip_next_assistant = False
            continue

        prefix = "USER" if role == "user" else "VOX"
        exchanges.append(f"[{prefix}]: {text}")

    combined = "\n\n".join(exchanges)
    # Trim if too long — keep the tail (most recent)
    if len(combined) > MAX_NEW_CHARS:
        combined = "...[earlier content trimmed]...\n\n" + combined[-MAX_NEW_CHARS:]

    return combined, total_lines


# ---------------------------------------------------------------------------
# Working memory supplement
# ---------------------------------------------------------------------------

def get_working_supplement() -> str:
    """Return WORKING.md content as supplementary context (may be empty)."""
    if not WORKING_MD.exists():
        return ""
    raw = WORKING_MD.read_text(encoding="utf-8")
    idx = raw.find(HEADER_SENTINEL)
    content = raw[idx + len(HEADER_SENTINEL):] if idx != -1 else raw
    content = content.strip()
    if not content or re.fullmatch(r"[-\s]*", content):
        return ""
    return content


# ---------------------------------------------------------------------------
# Memory context
# ---------------------------------------------------------------------------

def load_memory_context() -> str:
    """Load MEMORY.md index only — avoids sending all 59 files as input tokens.
    Full file contents are NOT loaded; the index descriptions are sufficient for
    deduplication and most contradiction detection."""
    if MEMORY_INDEX.exists():
        return "=== MEMORY.md INDEX ===\n" + MEMORY_INDEX.read_text(encoding="utf-8")
    return ""


# ---------------------------------------------------------------------------
# Haiku call
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are Vox's memory extractor. Given recent conversation excerpts and existing memory files, your job is to:
1. Identify facts worth persisting to long-term memory
2. Detect contradictions between new facts and existing memory

Memory types:
- **user**: facts about Corey — role, goals, preferences, knowledge (positive/helpful only)
- **feedback**: guidance on how Vox should behave. Lead with the rule, then **Why:** and **How to apply:** lines.
- **project**: ongoing work facts. Lead with fact, then **Why:** and **How to apply:** lines.
- **reference**: pointers to external resources (URLs, tools, service locations)

What NOT to save:
- Code patterns, file paths, or architecture (derivable from codebase)
- Ephemeral task details that will resolve this session
- Anything already captured verbatim in the existing memory shown below
- Obvious/generic facts

Memory file format:
---
name: descriptive-name
description: one-line description
type: user | feedback | project | reference
---
[content]

File names: kebab-case

Contradiction detection:
- If new content contradicts an existing memory file, flag it
- Only flag HIGH confidence contradictions (clear factual conflict, not just updates)
- Include the existing file name, old fact, and new fact

Return ONLY valid JSON, no markdown fencing:
{
  "operations": [
    {"action": "create", "filename": "example.md", "frontmatter": {"name": "...", "description": "...", "type": "..."}, "content": "..."},
    {"action": "update", "filename": "existing.md", "content": "...full new file content after frontmatter..."},
    {"action": "append", "filename": "promises.md", "content": "- [YYYY-MM-DD] ..."}
  ],
  "index_additions": [
    "- [Title](filename.md) — one-line hook under 150 chars"
  ],
  "contradictions": [
    {"file": "user-profile.md", "old_fact": "...", "new_fact": "...", "confidence": "high"}
  ]
}

Use "update" when a specific existing file has stale content that should be replaced.
Use "create" for genuinely new memory files.
Only add to index_additions for "create" operations.
If nothing is worth saving, return {"operations": [], "index_additions": [], "contradictions": []}.
"""


def call_haiku(api_key: str, new_content: str, memory_context: str) -> dict:
    try:
        import anthropic
    except ImportError:
        log("ERROR: 'anthropic' package not installed. Run: pip install anthropic")
        return {}

    client = anthropic.Anthropic(api_key=api_key)

    user_msg = f"""## Existing Memory (do not duplicate, detect contradictions)

{memory_context}

---

## New Conversation Content (extract what's worth saving)

{new_content}

---

Extract new facts worth persisting. Flag any contradictions with existing memory."""

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_msg}]
        )
        raw = response.content[0].text.strip()
        if raw.startswith("```"):
            raw = re.sub(r"^```\w*\n?", "", raw)
            raw = re.sub(r"\n?```$", "", raw)
        return json.loads(raw)
    except json.JSONDecodeError as e:
        log(f"JSON parse error: {e}")
        return {}
    except Exception as e:
        log(f"Haiku API error: {e}")
        return {}


# ---------------------------------------------------------------------------
# File operations
# ---------------------------------------------------------------------------

def build_file_content(frontmatter: dict, content: str) -> str:
    lines = ["---"]
    lines.append(f"name: {frontmatter.get('name', 'unnamed')}")
    lines.append(f"description: {frontmatter.get('description', '')}")
    lines.append(f"type: {frontmatter.get('type', 'user')}")
    lines.append("---")
    lines.append("")
    lines.append(content.strip())
    lines.append("")
    return "\n".join(lines)


def update_file_content(target: Path, new_body: str):
    """Replace body of existing memory file, preserving frontmatter."""
    if not target.exists():
        return
    existing = target.read_text(encoding="utf-8")
    # Find end of frontmatter
    if existing.startswith("---"):
        end = existing.find("---", 3)
        if end != -1:
            frontmatter_block = existing[:end + 3]
            target.write_text(frontmatter_block + "\n\n" + new_body.strip() + "\n", encoding="utf-8")
            return
    # No frontmatter — just replace
    target.write_text(new_body.strip() + "\n", encoding="utf-8")


def execute_operations(operations: list, index_additions: list) -> tuple[list, list]:
    created, updated_appended = [], []

    for op in operations:
        action   = op.get("action", "")
        filename = op.get("filename", "")
        if not filename:
            continue
        target = MEMORY_DIR / filename

        if action == "create":
            if target.exists():
                log(f"SKIP create (exists): {filename}")
                continue
            fm = op.get("frontmatter", {})
            target.write_text(build_file_content(fm, op.get("content", "")), encoding="utf-8")
            created.append(filename)
            log(f"Created: {filename}")

        elif action == "update":
            if not target.exists():
                log(f"SKIP update (not found): {filename}")
                continue
            update_file_content(target, op.get("content", ""))
            updated_appended.append(f"updated:{filename}")
            log(f"Updated: {filename}")

        elif action == "append":
            content = op.get("content", "").strip()
            if not content:
                continue
            if target.exists():
                existing = target.read_text(encoding="utf-8")
                target.write_text(existing.rstrip() + "\n" + content + "\n", encoding="utf-8")
            else:
                target.write_text(content + "\n", encoding="utf-8")
            updated_appended.append(f"appended:{filename}")
            log(f"Appended to: {filename}")

    # Update MEMORY.md index
    if index_additions and MEMORY_INDEX.exists():
        index = MEMORY_INDEX.read_text(encoding="utf-8").rstrip()
        for entry in index_additions:
            entry = entry.strip()
            if entry and entry not in index:
                index += "\n" + entry
        MEMORY_INDEX.write_text(index + "\n", encoding="utf-8")
        log(f"Index updated with {len(index_additions)} addition(s)")

    return created, updated_appended


# ---------------------------------------------------------------------------
# Contradiction queue
# ---------------------------------------------------------------------------

def write_contradictions(contradictions: list):
    if not contradictions:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [f"\n## {timestamp}\n"]
    for c in contradictions:
        if c.get("confidence", "") != "high":
            continue
        lines.append(f"**File:** `{c.get('file', '?')}`")
        lines.append(f"**Existing fact:** {c.get('old_fact', '?')}")
        lines.append(f"**New info:** {c.get('new_fact', '?')}")
        lines.append(f"**Resolve:** Which is current? Reply and I'll update memory.")
        lines.append("")

    if len(lines) <= 1:
        return  # Only header, no high-confidence contradictions

    if not CONTRADICTIONS_MD.exists():
        header = "# Pending Memory Contradictions\n> Vox checks this at session start. Each entry needs Corey's resolution.\n"
        CONTRADICTIONS_MD.write_text(header, encoding="utf-8")

    existing = CONTRADICTIONS_MD.read_text(encoding="utf-8")
    CONTRADICTIONS_MD.write_text(existing.rstrip() + "\n" + "\n".join(lines), encoding="utf-8")
    log(f"Wrote {len(contradictions)} contradiction(s) to pending queue")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    log("=== vox-memory-writer v2 start ===")

    # Read hook payload from stdin (or fall back to CLI arg)
    transcript_path = None
    session_id = None

    if not sys.stdin.isatty():
        try:
            payload = json.loads(sys.stdin.read())
            transcript_path = payload.get("transcript_path", "")
            session_id = payload.get("session_id", "")
        except Exception:
            pass

    # CLI override: --transcript <path>
    if "--transcript" in sys.argv:
        idx = sys.argv.index("--transcript")
        if idx + 1 < len(sys.argv):
            transcript_path = sys.argv[idx + 1]
            session_id = session_id or "manual"

    if not transcript_path:
        log("No transcript_path — nothing to process.")
        return

    if not session_id:
        session_id = Path(transcript_path).stem

    api_key = load_api_key()
    if not api_key:
        log("ERROR: No API key. Add ANTHROPIC_API_KEY to .claude/config/anthropic.env")
        return

    # Read new transcript content
    new_content, total_lines = read_new_transcript_lines(transcript_path, session_id)

    # Supplement with WORKING.md if available
    working = get_working_supplement()
    if working:
        new_content = new_content + "\n\n=== WORKING.md NOTES ===\n" + working if new_content else working

    if not new_content.strip():
        log("No new content to process.")
        save_position(session_id, total_lines)
        return

    if len(new_content.strip()) < MIN_MEANINGFUL_CHARS:
        log(f"Skipping — content too short after filtering ({len(new_content)} chars < {MIN_MEANINGFUL_CHARS})")
        save_position(session_id, total_lines)
        return

    log(f"New content: {len(new_content)} chars | Total transcript lines: {total_lines}")

    memory_context = load_memory_context()
    result = call_haiku(api_key, new_content, memory_context)

    if not result:
        log("No result from Haiku.")
        save_position(session_id, total_lines)
        return

    operations       = result.get("operations", [])
    index_additions  = result.get("index_additions", [])
    contradictions   = result.get("contradictions", [])

    log(f"Haiku: {len(operations)} op(s), {len(contradictions)} contradiction(s)")

    if operations:
        created, others = execute_operations(operations, index_additions)
        log(f"Done — created: {created}, other: {others}")
    else:
        log("Nothing to save.")

    write_contradictions(contradictions)
    save_position(session_id, total_lines)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        log(f"FATAL:\n{traceback.format_exc()}")
        sys.exit(1)
