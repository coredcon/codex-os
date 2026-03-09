# /today — Morning Planning

Generate a prioritized plan for today by pulling together all available context.

## Steps

1. Get today's date and day name
2. Read today's daily note if it exists (`01 Daily/YYYY/MM/YYYY-MM-DD.md`) — create it from the template if not
3. Read `VAULT-INDEX.md` for the ONE Big Thing and active projects
4. Check personal Google Calendar for today's events
5. Parse `06 Resources/Work/work-calendar.ics` for today's work meetings (use Python with icalendar + recurring_ical_events)
6. Check `00 Inbox/` for any unprocessed items
7. Fetch weather: `curl -s "wttr.in/47130?format=3"` for today, then `curl -s "wttr.in/47130?format=%t+%C&period=1"` for a 3-day outlook. (ZIP 47130 = Jeffersonville, IN)
8. Check `04 Home/Honey-Do/honey-do.md` for any active outdoor tasks

## Output format

```
## TODAY — [Day], [Date]

**ONE Big Thing:** [from VAULT-INDEX]

**Meetings:**
- [time] [event] (work/personal)

**Inbox:** [count] items waiting

**Weather:** [today's condition + temp] | Next 3 days: [brief outlook]
[If outdoor tasks exist in Honey-Do: flag each one as ✅ good day / 🌧 skip it]

**Focus blocks:**
- [suggested 1-3 focus blocks based on gaps between meetings]

**Carry-overs:** [any unfinished items from yesterday's daily note]
```

Keep it scannable. Max 3 focus items. If there are no meetings, say so and suggest a full focus block. Flag if today is Wednesday (office day).
When Corey mentions an outdoor plan ("I want to mow this weekend", "thinking of working in the garage Saturday"), check the forecast and give a direct yes/no on whether the weather supports it.
