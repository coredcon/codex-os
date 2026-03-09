#!/bin/bash
# Vox PreToolUse Hook — Protect Archive
# Blocks any write/edit to files inside 07 Archive/
# Uses grep on raw JSON — no python3 dependency, fast startup

INPUT=$(cat)

if echo "$INPUT" | grep -q "07 Archive"; then
  echo "BLOCKED: Cannot modify archived files. Move to the appropriate Projects or Areas folder first if you need to edit this."
  exit 2
fi

exit 0
