#!/usr/bin/env python3
"""
vox-overnight.py

Runs nightly via Task Scheduler (~5 AM) to:
1. Generate tomorrow's daily note pre-filled with carried tasks and work events.
2. Write .claude/session-brief.md — a pre-digested startup file so Vox reads
   one file at session start instead of 8+ individual sources.

Setup:
- Update the path constants below to match your vault location
- Schedule via Task Scheduler (Windows) or cron (Linux/Mac)
- Optional integrations: Freshdesk (work tickets), ICS (work calendar)

Logs output to: .claude/scripts/vox-overnight.log
"""

import os
import re
import sys
import traceback
from datetime import datetime, timedelta, date
from pathlib import Path

# ── Configuration — update these paths ────────────────────────────────────────
VAULT_ROOT    = Path(r"[YOUR_VAULT_PATH]")
DAILY_DIR     = VAULT_ROOT / "01 Daily"

# Optional: work calendar ICS file (export from Google Calendar, Outlook, etc.)
# Place at this path to get work events in the daily note and session brief
ICS_PATH      = VAULT_ROOT / "06 Resources" / "Work" / "work-calendar.ics"

# Optional: async instruction drop folder (files dropped here are processed by Vox at session start)
# Leave as empty Path to disable: ASYNC_DROP = Path("")
ASYNC_DROP    = Path(r"[YOUR_ASYNC_DROP_FOLDER]")

REFLECTION    = VAULT_ROOT / ".claude" / "pending-reflection.md"
LOG_FILE      = VAULT_ROOT / ".claude" / "scripts" / "vox-overnight.log"
SESSION_BRIEF = VAULT_ROOT / ".claude" / "session-brief.md"
VAULT_INDEX   = VAULT_ROOT / "VAULT-INDEX.md"
HONEY_DO      = VAULT_ROOT / "04 Home" / "Honey-Do" / "honey-do.md"
STATE_FILE    = VAULT_ROOT / ".claude" / "state.md"

# Optional: Freshdesk integration — configure config/freshdesk.env to enable
FRESHDESK_ENV = VAULT_ROOT / ".claude" / "config" / "freshdesk.env"

# Timezone for calendar parsing (IANA format)
LOCAL_TIMEZONE = "America/New_York"
# ──────────────────────────────────────────────────────────────────────────────


def log(msg: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)


def daily_note_path(d: date) -> Path:
    return DAILY_DIR / str(d.year) / f"{d.month:02d}" / f"{d.strftime('%Y-%m-%d')}.md"


def get_unchecked_tasks(note_path: Path) -> list:
    """Extract up to 3 unchecked tasks from a daily note."""
    if not note_path.exists():
        return []
    content = note_path.read_text(encoding="utf-8")
    tasks = re.findall(r"^- \[ \] (.+)$", content, re.MULTILINE)
    return tasks[:3]


def get_work_events(target: date) -> list:
    """Return formatted work event strings for target date from ICS."""
    if not ICS_PATH.exists():
        log(f"ICS not found at {ICS_PATH}")
        return []
    try:
        import icalendar
        import recurring_ical_events

        with open(ICS_PATH, "rb") as f:
            cal = icalendar.Calendar.from_ical(f.read())

        start_dt = datetime(target.year, target.month, target.day, 0, 0, 0)
        end_dt   = datetime(target.year, target.month, target.day, 23, 59, 59)
        events   = recurring_ical_events.of(cal).between(start_dt, end_dt)

        from zoneinfo import ZoneInfo
        local_tz = ZoneInfo(LOCAL_TIMEZONE)

        results = []
        for ev in events:
            summary = str(ev.get("SUMMARY", "Unknown"))
            dtstart = ev.get("DTSTART").dt
            if hasattr(dtstart, "hour"):
                if dtstart.tzinfo is not None:
                    dtstart = dtstart.astimezone(local_tz)
                time_str = dtstart.strftime("%I:%M %p").lstrip("0") or "12:00 AM"
                results.append((dtstart.hour * 60 + dtstart.minute, f"{time_str} — {summary}"))
            else:
                results.append((-1, f"All day — {summary}"))

        results.sort(key=lambda x: x[0])
        return [r[1] for r in results]

    except Exception as e:
        log(f"ICS parse error: {e}")
        return [f"(calendar error — check ICS file)"]


def build_note(target: date, tasks: list, events: list) -> str:
    day_name  = target.strftime("%A")
    date_str  = target.strftime("%Y-%m-%d")
    date_long = target.strftime("%A, %B %-d, %Y")   # Use %#d on Windows

    task_lines = [f"- [ ] {t}" for t in tasks]
    while len(task_lines) < 3:
        task_lines.append("- [ ]")

    if events:
        scheduled = "### Scheduled\n" + "\n".join(f"- {e}" for e in events) + "\n\n-"
    else:
        scheduled = "-"

    return f"""---
date: {date_str}
day: {day_name}
energy:
mood:
---

# {date_long}

## Morning Check-In
> Start here first. Takes 3 minutes. Don't skip it.

**ONE Thing today:**

**Brain dump (what's on my mind right now):**
-

**Top 3 tasks (max 3 — pick carefully):**
{chr(10).join(task_lines)}

---

## Log
> Drop everything here as the day happens. Notes, ideas, links, observations. No organization needed.

{scheduled}

---

## Home / Family
> Anything the house or family needs today.

-

---

## Evening Close
> 5 minutes. Closes the day.

**Done today:**
-

**Unfinished (move to tomorrow or Inbox):**
-

**One thing I learned or noticed:**

**Tomorrow's ONE Thing:**

---

## Captured
> Raw capture bin — links, ideas, quotes to process later. Don't organize now.

---

## Vox Session Digest
> Written by Vox at session end. Do not edit manually.

### Context


### Decisions


### Facts Learned


### Related Projects


### Keywords


"""


def append_reflection(msg: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"- [{timestamp}] `overnight-brief` \U0001f319 {msg}\n"
    with open(REFLECTION, "a", encoding="utf-8") as f:
        f.write(entry)


# ── Session Brief helpers ──────────────────────────────────────────────────────

def extract_vault_index_sections() -> dict:
    """Pull ONE Big Thing, active projects table, and inbox status from VAULT-INDEX.md."""
    result = {"one_big_thing": "", "projects": "", "inbox": ""}
    if not VAULT_INDEX.exists():
        return result
    content = VAULT_INDEX.read_text(encoding="utf-8")

    m = re.search(r"## This Week.s ONE Big Thing\n.*?\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
    if m:
        result["one_big_thing"] = m.group(1).strip()

    m = re.search(r"## Active Projects\n((?:\|.*\n?)+)", content)
    if m:
        result["projects"] = m.group(1).strip()

    inbox_section = re.search(r"## Inbox.*?(?=\n## |\Z)", content, re.DOTALL)
    if inbox_section:
        s = inbox_section.group(0)
        count_m   = re.search(r"Count:\s*(\d+|unknown)", s)
        proc_m    = re.search(r"Last processed:\s*(.+)", s)
        count     = count_m.group(1) if count_m else "unknown"
        processed = proc_m.group(1).strip() if proc_m else "unknown"
        result["inbox"] = f"- Count: {count}\n- Last processed: {processed}"
    else:
        result["inbox"] = "- Count: unknown"

    return result


def extract_honey_do() -> str:
    """Return active honey-do items."""
    if not HONEY_DO.exists():
        return "- (file not found)"
    content = HONEY_DO.read_text(encoding="utf-8")
    m = re.search(r"## Active\n((?:- .+\n?)+)", content)
    if m:
        return m.group(1).strip()
    return "- (none)"


def extract_recent_facts(today: date) -> str:
    """Pull Facts Learned sections from last 3 daily notes."""
    facts = []
    for delta in range(0, 4):
        d = today - timedelta(days=delta)
        path = daily_note_path(d)
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        for m in re.finditer(r"### Facts Learned\n((?:- .+\n?)+)", content):
            block = m.group(1).strip()
            if block and block != "-":
                facts.append(f"**{d.strftime('%Y-%m-%d')}**\n{block}")
        if len(facts) >= 3:
            break
    return "\n\n".join(facts) if facts else "- (none in last 3 days)"


def count_async_drop() -> int:
    """Count files in async drop folder."""
    if not ASYNC_DROP or not ASYNC_DROP.exists():
        return 0
    return len([f for f in ASYNC_DROP.iterdir() if f.is_file()])


def get_freshdesk_tickets() -> str:
    """
    Pull open/pending tickets assigned to you from Freshdesk.

    Requires config/freshdesk.env with:
        FRESHDESK_DOMAIN=yourcompany.freshdesk.com
        FRESHDESK_API_KEY=your_api_key
        FRESHDESK_AGENT_ID=your_agent_id
    """
    if not FRESHDESK_ENV.exists():
        return "- (freshdesk.env not configured — see config/freshdesk.env.example)"
    try:
        import urllib.request, urllib.error, base64, json, urllib.parse
        config = {}
        for line in FRESHDESK_ENV.read_text().splitlines():
            if '=' in line and not line.startswith('#'):
                k, v = line.split('=', 1)
                config[k.strip()] = v.strip()

        domain    = config.get('FRESHDESK_DOMAIN', '')
        api_key   = config.get('FRESHDESK_API_KEY', '')
        agent_id  = config.get('FRESHDESK_AGENT_ID', '')

        creds   = base64.b64encode(f'{api_key}:X'.encode()).decode()
        headers = {'Authorization': f'Basic {creds}'}

        active_statuses = [9,27,18,44,2,3,39,37,30,53,52,54,26,20,55,49,50,51,19,33,35,22,29,28,56,57,59,25,58]
        status_q = ' OR '.join(f'status:{s}' for s in active_statuses)
        query    = f'agent_id:{agent_id} AND ({status_q})'
        encoded  = urllib.parse.quote(query)
        url      = f'https://{domain}/api/v2/search/tickets?query="{encoded}"'
        req     = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=10) as resp:
            data    = json.loads(resp.read())
            tickets = data.get('results', [])

        CLOSED_STATUSES = {4, 5}
        active = [t for t in tickets if t.get('status') not in CLOSED_STATUSES]
        if not active:
            return "- ✅ No active tickets assigned"

        lines = [f"- Active assigned: {len(active)} ticket(s)"]
        for t in active:
            lines.append(f"  - #{t['id']} {t['subject'][:65]}")

        return "\n".join(lines)

    except Exception as e:
        log(f"Freshdesk error: {e}")
        return f"- (error fetching tickets: {e})"


def git_backup():
    """Stage all changes and push to GitHub."""
    import subprocess
    vault = str(VAULT_ROOT)
    date_str = datetime.now().strftime("%Y-%m-%d")
    try:
        subprocess.run(["git", "-C", vault, "add", "."], check=True, capture_output=True)
        result = subprocess.run(
            ["git", "-C", vault, "commit", "-m", f"nightly backup {date_str}"],
            capture_output=True, text=True
        )
        if "nothing to commit" in result.stdout:
            log("Git: nothing to commit")
            return
        subprocess.run(["git", "-C", vault, "push"], check=True, capture_output=True)
        log(f"Git: backup pushed for {date_str}")
    except subprocess.CalledProcessError as e:
        log(f"Git backup error: {e.stderr or e}")


def generate_session_brief(today: date, tomorrow: date, tasks: list, events: list):
    """Write .claude/session-brief.md — pre-digested context for Vox startup."""
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    vi = extract_vault_index_sections()
    honey_do = extract_honey_do()
    facts = extract_recent_facts(today)
    async_count = count_async_drop()
    state = STATE_FILE.read_text(encoding="utf-8") if STATE_FILE.exists() else "(state.md not found)"

    tasks_md = "\n".join(f"- [ ] {t}" for t in tasks) if tasks else "- (none carried)"
    events_md = "\n".join(f"- {e}" for e in events) if events else "- (no ICS events)"
    async_md = f"Count: {async_count}" + (" — ⚠️ FILES WAITING — read and act at session start" if async_count > 0 else " — clear")

    freshdesk = get_freshdesk_tickets()

    content = f"""# Vox Session Brief — {tomorrow.strftime('%Y-%m-%d')}
> Generated: {generated_at} by vox-overnight.py
> ⚠️ Live data still needed at startup: personal calendar + work freeBusy
> This file replaces startup reads of: VAULT-INDEX, project files, honey-do, ICS parse, recent daily notes

---

## ONE Big Thing This Week
{vi["one_big_thing"] or "(not set — check VAULT-INDEX.md)"}

## Inbox
{vi["inbox"]}

## Work — Tickets (if configured)
{freshdesk}

## Carried Tasks (from {today.strftime('%Y-%m-%d')})
{tasks_md}

## Work Calendar — {tomorrow.strftime('%Y-%m-%d')} (ICS)
{events_md}

## Active Projects
{vi["projects"] or "(could not parse — check VAULT-INDEX.md)"}

## Home / Honey-Do
{honey_do}

## Async Drop
{async_md}

## State
{state}

## Recent Facts Learned (last 3 days)
{facts}

---
*If this file is >24h old, treat it as stale and fall back to reading source files.*
"""

    SESSION_BRIEF.write_text(content, encoding="utf-8")
    log(f"Session brief written to {SESSION_BRIEF}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    today      = date.today()
    tomorrow   = today + timedelta(days=1)
    note_path  = daily_note_path(tomorrow)
    today_path = daily_note_path(today)
    tasks      = get_unchecked_tasks(today_path)
    events     = get_work_events(tomorrow)

    # 1. Daily note (skip if already exists)
    if note_path.exists():
        log(f"Daily note already exists for {tomorrow} — skipping note creation")
    else:
        content = build_note(tomorrow, tasks, events)
        note_path.parent.mkdir(parents=True, exist_ok=True)
        note_path.write_text(content, encoding="utf-8")
        log(f"Daily note created for {tomorrow}")

    # 2. Session brief (always regenerate — it's Vox's startup cache)
    generate_session_brief(today, tomorrow, tasks, events)

    carried   = f"{len(tasks)} task(s) carried" if tasks else "no tasks carried"
    scheduled = f"{len(events)} work event(s)" if events else "no work events"
    summary   = f"Pre-brief generated for {tomorrow.strftime('%Y-%m-%d')} — {carried}, {scheduled}"

    append_reflection(summary)
    log(summary)

    # 3. Git backup
    git_backup()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        log(f"FATAL ERROR:\n{traceback.format_exc()}")
        sys.exit(1)
