#!/bin/bash
# Vox Stop Hook — snapshot WORKING.md content at end of every response
# If WORKING.md has substantive content, save a timestamped copy to .claude/snapshots/
# The next session's init hook will detect this and process it via Haiku.

WORKING="F:/My Drive/Obsidian/Codex.os/.claude/WORKING.md"
SNAPDIR="F:/My Drive/Obsidian/Codex.os/.claude/snapshots"

mkdir -p "$SNAPDIR"

# Count lines — WORKING.md header alone is ~10 lines; only snapshot if there's real content
LINECOUNT=$(wc -l < "$WORKING" 2>/dev/null || echo 0)

if [ "$LINECOUNT" -gt 10 ]; then
  STAMP=$(date +%Y%m%d-%H%M%S)
  cp "$WORKING" "$SNAPDIR/$STAMP.md"
fi
