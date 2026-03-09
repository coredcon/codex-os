#!/bin/bash
# Vox PostToolUse Hook — Auto Commit
# Fires after every file write/edit. Keeps vault version-controlled automatically.

VAULT="F:/My Drive/Obsidian/Codex.os"

cd "$VAULT" 2>/dev/null || exit 0

# Only run if this is a git repo
if [ ! -d ".git" ]; then
  exit 0
fi

# Stage and commit
git add -A
CHANGED=$(git diff --cached --name-only 2>/dev/null)

if [ -n "$CHANGED" ]; then
  git commit -m "Vox: auto-save $(date +%Y-%m-%dT%H:%M)" --quiet 2>/dev/null
fi

exit 0
