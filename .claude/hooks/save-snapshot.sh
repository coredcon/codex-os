#!/bin/bash
# Vox Stop Hook — runs after every Claude response
# 1. Snapshots WORKING.md if it has substantive content
# 2. Runs vox-extract.py to extract facts from transcript into queue
# 3. Triggers throttled QMD reindex

# Capture stdin (hook data JSON from Claude Code)
HOOK_DATA=$(cat)

WORKING="F:/My Drive/Obsidian/Codex.os/.vox-working.md"
SNAPDIR="F:/My Drive/Obsidian/Codex.os/.claude/snapshots"

mkdir -p "$SNAPDIR"

# Snapshot WORKING.md if it has real content (header alone is ~10 lines)
LINECOUNT=$(wc -l < "$WORKING" 2>/dev/null || echo 0)
if [ "$LINECOUNT" -gt 10 ]; then
  STAMP=$(date +%Y%m%d-%H%M%S)
  cp "$WORKING" "$SNAPDIR/$STAMP.md"
fi

# Run extraction — pipe hook data so vox-extract.py gets transcript_path
echo "$HOOK_DATA" | python "F:/My Drive/Obsidian/Codex.os/.claude/scripts/vox-extract.py" &

# Keep snapshots directory lean — keep only last 20
ls -t "$SNAPDIR"/*.md 2>/dev/null | tail -n +21 | xargs rm -f 2>/dev/null || true
