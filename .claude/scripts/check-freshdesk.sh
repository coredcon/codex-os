#!/usr/bin/env bash
# check-freshdesk.sh — silent Freshdesk diff check
# Outputs ONLY if there are new NEEDS RESPONSE tickets or status changes since last run.

set -euo pipefail

DOMAIN="qsrautomations.freshdesk.com"
API_KEY="rJ2cCU5I4jbjyJXGVDqF"
AGENT_ID="17001810126"
STATE_FILE="F:/My Drive/Obsidian/Codex.os/.claude/state/freshdesk-last-check.txt"
SNAPSHOT_FILE="F:/My Drive/Obsidian/Codex.os/.claude/state/freshdesk-snapshot.json"

NOW=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
LAST_CHECK=$(cat "$STATE_FILE" 2>/dev/null | head -1 | tr -d '[:space:]' || echo "2000-01-01T00:00:00Z")

# Fetch tickets updated since last check, assigned to this agent
RESPONSE=$(curl -s -u "${API_KEY}:X" \
  "https://${DOMAIN}/api/v2/search/tickets?query=%22agent_id%3A${AGENT_ID}%22&include=stats" \
  -H "Content-Type: application/json" 2>/dev/null || echo '{"results":[]}')

# Extract tickets updated since last check
UPDATED=$(echo "$RESPONSE" | python3 -c "
import sys, json
data = json.load(sys.stdin)
tickets = data.get('results', [])
last = '$LAST_CHECK'
updates = []
for t in tickets:
    updated = t.get('updated_at', '')
    if updated > last:
        status_map = {2:'Open', 3:'Pending', 5:'Resolved', 4:'Closed', 6:'Waiting on Customer', 7:'Waiting on Third Party'}
        status = status_map.get(t.get('status', 0), str(t.get('status', '?')))
        subject = t.get('subject', '')[:60]
        tid = t.get('id', '?')
        updates.append(f'#{tid} [{status}] {subject}')
if updates:
    print('Freshdesk updates since last check:')
    for u in updates:
        print(f'  {u}')
" 2>/dev/null)

# Update timestamp
echo "$NOW" > "$STATE_FILE"

# Output only if there are updates
if [ -n "$UPDATED" ]; then
    echo "$UPDATED"
fi
