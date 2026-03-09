#!/bin/bash
# Vox UserPromptSubmit Hook — Session Briefing
# Fires on first prompt only, using a temp flag file.

FLAG="/tmp/vox-session-started.flag"

# Only run once per session
if [ -f "$FLAG" ]; then
  exit 0
fi
touch "$FLAG"

VAULT="F:/My Drive/Obsidian/Codex.os"

# ANSI colors
AMBER='\033[38;5;214m'
GOLD='\033[1;33m'
CYAN='\033[36m'
GREEN='\033[32m'
YELLOW='\033[1;33m'
RED='\033[31m'
DIM='\033[2m'
BOLD='\033[1m'
RESET='\033[0m'

# Use explicit path to date from Git Bash
TODAY=$(/usr/bin/date +%Y-%m-%d)
DAY_NAME=$(/usr/bin/date +%A)
TIME_NOW=$(/usr/bin/date +%H:%M)
MONTH=$(/usr/bin/date +%m)
YEAR=$(/usr/bin/date +%Y)
WEEKNUM=$(/usr/bin/date +%V)
WEEK_LABEL="${YEAR}-W${WEEKNUM}"

DAILY_NOTE="${VAULT}/01 Daily/${YEAR}/${MONTH}/${TODAY}.md"
WEEKLY_NOTE="${VAULT}/02 Weekly/${WEEK_LABEL}.md"

INBOX_COUNT=$(find "${VAULT}/00 Inbox" -name "*.md" 2>/dev/null | wc -l)
HONEY_DO_COUNT=$(find "${VAULT}/04 Home/Honey-Do" -name "*.md" -not -name "README.md" 2>/dev/null | wc -l)

printf "${AMBER}╔══════════════════════════════════════╗${RESET}\n"
printf "${AMBER}  VOX ONLINE${RESET} ${DIM}—${RESET} ${BOLD}${DAY_NAME}, ${TODAY}${RESET} ${DIM}${TIME_NOW}${RESET}\n"
printf "${AMBER}╚══════════════════════════════════════╝${RESET}\n"
printf "\n"

# Daily note status
if [ ! -f "$DAILY_NOTE" ]; then
  printf "  ${YELLOW}⚠  No daily note for today yet${RESET}\n"
else
  printf "  ${GREEN}✓${RESET}  Daily note ready\n"
fi

# Weekly note status
[ ! -f "$WEEKLY_NOTE" ] && printf "  ${DIM}○  No weekly review for ${WEEK_LABEL} yet${RESET}\n"

# Inbox
[ "$INBOX_COUNT" -gt 0 ] && printf "  ${YELLOW}📥 INBOX: ${INBOX_COUNT} item(s) need processing${RESET}\n"

# Honey-do
[ "$HONEY_DO_COUNT" -gt 0 ] && printf "  ${DIM}🏠 HONEY-DO: ${HONEY_DO_COUNT} item(s)${RESET}\n"

# ONE Big Thing
if [ -f "${VAULT}/VAULT-INDEX.md" ]; then
  ONE_BIG=$(grep -A 3 "ONE Big Thing" "${VAULT}/VAULT-INDEX.md" | grep -v "ONE Big Thing" | grep -v "^>" | grep -v "^$" | grep -v "^-" | head -1 | sed 's/^[[:space:]]*//')
  if [ -n "$ONE_BIG" ] && [ "$ONE_BIG" != "—" ]; then
    printf "\n  ${AMBER}★  ${BOLD}${ONE_BIG}${RESET}\n"
  fi
fi

# Office day
[ "$DAY_NAME" = "Wednesday" ] && printf "\n  ${YELLOW}${BOLD}⚡ OFFICE DAY — Don't forget you're in today.${RESET}\n"

# Work calendar from ICS
WORK_CAL="${VAULT}/06 Resources/Work/work-calendar.ics"
if [ -f "$WORK_CAL" ]; then
  python3 - <<'PYEOF'
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

AMBER  = '\033[38;5;214m'
CYAN   = '\033[36m'
GREEN  = '\033[32m'
YELLOW = '\033[1;33m'
DIM    = '\033[2m'
BOLD   = '\033[1m'
RESET  = '\033[0m'

try:
    import icalendar, recurring_ical_events
    from datetime import date, datetime, timezone, timedelta

    vault = "F:/My Drive/Obsidian/Codex.os"
    ics_path = f"{vault}/06 Resources/Work/work-calendar.ics"

    with open(ics_path, 'rb') as f:
        cal = icalendar.Calendar.from_ical(f.read())

    today = date.today()
    tomorrow = today + timedelta(days=1)
    window_start = datetime(today.year, today.month, today.day, 0, 0, tzinfo=timezone.utc)
    window_end   = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 23, 59, tzinfo=timezone.utc)

    events = recurring_ical_events.of(cal).between(window_start, window_end)

    seen = set()
    results = []
    for e in events:
        summary  = str(e.get('SUMMARY', 'No title')).strip()
        dtstart  = e.get('DTSTART').dt
        if isinstance(dtstart, datetime):
            dt_date  = dtstart.date()
            time_str = dtstart.astimezone().strftime('%I:%M %p').lstrip('0')
        else:
            dt_date  = dtstart
            time_str = 'All day'
        key = (dt_date, summary)
        if key not in seen:
            seen.add(key)
            label = 'TODAY' if dt_date == today else 'TMW'
            results.append((dt_date, label, time_str, summary))

    results.sort()
    if results:
        print(f'\n  {AMBER}WORK CALENDAR{RESET}')
        for _, label, t, s in results:
            color = GREEN if label == 'TODAY' else CYAN
            print(f'  {color}[{label}]{RESET} {t} {DIM}—{RESET} {s}')
    else:
        print(f'\n  {DIM}WORK: No meetings today or tomorrow{RESET}')
except ImportError:
    print(f'\n  \033[31mWORK CAL: pip install icalendar recurring-ical-events\033[0m')
except Exception:
    pass
PYEOF
else
  printf "\n  ${DIM}WORK CALENDAR: Drop ICS → 06 Resources/Work/work-calendar.ics${RESET}\n"
fi

printf "\n"
