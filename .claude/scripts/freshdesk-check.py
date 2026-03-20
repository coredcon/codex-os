#!/usr/bin/env python3
"""
freshdesk-check.py
Checks for Freshdesk ticket updates since last run. Designed for use with /loop.

Usage:
    python freshdesk-check.py          # check my active tickets for updates since last run
    python freshdesk-check.py --reset  # reset last-check timestamp to now
    python freshdesk-check.py --all    # show all my active (non-closed/resolved) tickets

State file: .claude/state/freshdesk-last-check.txt
"""

import sys
import io
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# --- Config ---
SCRIPT_DIR = Path(__file__).parent
VAULT_DIR = SCRIPT_DIR.parent
ENV_FILE = VAULT_DIR / "config" / "freshdesk.env"
STATE_FILE = VAULT_DIR / "state" / "freshdesk-last-check.txt"

# All non-closed/resolved status codes for this Freshdesk instance
# (excludes 4=Resolved, 5=Closed — confirmed against full status list from API)
ACTIVE_STATUSES = [9,27,18,44,2,3,39,37,30,53,52,54,26,20,55,49,50,51,19,33,35,22,29,28,56,57,59,25,58]

def load_env():
    env = {}
    with open(ENV_FILE) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env

def get_last_check():
    if STATE_FILE.exists():
        ts = STATE_FILE.read_text().strip()
        try:
            return datetime.fromisoformat(ts)
        except ValueError:
            pass
    return datetime.now(timezone.utc) - timedelta(hours=24)

def save_last_check():
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(datetime.now(timezone.utc).isoformat())

def fetch_my_active_tickets(domain, api_key, agent_id):
    """Fetch all non-closed tickets where I am the assigned agent."""
    status_part = " OR ".join(f"status:{s}" for s in ACTIVE_STATUSES)
    query = f'"agent_id:{agent_id} AND ({status_part})"'
    all_tickets = []
    for page in range(1, 11):
        r = requests.get(
            f"https://{domain}/api/v2/search/tickets",
            params={"query": query, "page": page},
            auth=(api_key, "X"),
            timeout=10,
        )
        r.raise_for_status()
        results = r.json().get("results", [])
        if not results:
            break
        # Belt-and-suspenders: drop any resolved/closed that slipped through
        all_tickets.extend(t for t in results if t.get("status") not in (4, 5))
        if len(results) < 30:
            break
    return all_tickets

STATUS_LABELS = {
    2: "Open", 3: "Pending", 4: "Resolved", 5: "Closed",
    6: "Waiting on Customer", 7: "Waiting on 3rd Party",
}

def status_label(s):
    return STATUS_LABELS.get(s, f"Status {s}")

def priority_label(p):
    return {1: "Low", 2: "Med", 3: "High", 4: "Urgent"}.get(p, str(p))

def format_ticket(t, highlight=False):
    status = status_label(t.get("status", 0))
    priority = priority_label(t.get("priority", 0))
    updated = t.get("updated_at", "")[:10]
    subject = t.get("subject", "(no subject)")[:55]
    tid = t.get("id")
    flag = "⚠️  " if highlight else "   "
    return f"{flag}#{tid} [{status}] [{priority}] {subject} (updated {updated})"

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    env = load_env()
    domain = env["FRESHDESK_DOMAIN"]
    api_key = env["FRESHDESK_API_KEY"]
    agent_id = env["FRESHDESK_AGENT_ID"]

    if mode == "--reset":
        save_last_check()
        print(f"Last-check reset to {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
        return

    tickets = fetch_my_active_tickets(domain, api_key, agent_id)
    tickets.sort(key=lambda t: t.get("updated_at", ""), reverse=True)

    if mode == "--all":
        print(f"My active tickets ({len(tickets)} total):\n")
        for t in tickets:
            print(format_ticket(t))
        return

    # Default: show only tickets updated since last check
    last_check = get_last_check()
    now = datetime.now(timezone.utc)
    elapsed_min = int((now - last_check).total_seconds() / 60)

    updated = []
    for t in tickets:
        upd_str = t.get("updated_at", "")
        try:
            upd_dt = datetime.fromisoformat(upd_str.replace("Z", "+00:00"))
            if upd_dt > last_check:
                updated.append((upd_dt, t))
        except Exception:
            pass

    save_last_check()

    if not updated:
        print(f"No updates on my Freshdesk tickets in the last {elapsed_min}m.")
        return

    updated.sort(key=lambda x: x[0], reverse=True)
    print(f"🔔 {len(updated)} ticket(s) updated in the last {elapsed_min}m:\n")
    for _, t in updated:
        needs_action = t.get("status") in (2, 6)
        print(format_ticket(t, highlight=needs_action))

if __name__ == "__main__":
    main()
