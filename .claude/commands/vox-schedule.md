# /schedule — Weekly Planning

Map this week's priorities to actual time blocks. Surface conflicts between what matters and how time is being spent.

## Steps

1. Get the current week (Mon–Sun dates)
2. Read `VAULT-INDEX.md` for ONE Big Thing, active projects, and areas
3. Read `02 Weekly/YYYY-Www.md` if it exists
4. Pull personal Google Calendar events for the full week
5. Parse `06 Resources/Work/work-calendar.ics` for work meetings this week (use Python with icalendar + recurring_ical_events)
6. Identify free blocks (90min+ gaps between meetings, excluding evenings)
7. Map active projects to free blocks based on stated priorities

## Output format

```
## Week of [Mon Date] — [Week Label]

**ONE Big Thing:** [from VAULT-INDEX]

**This week's meetings:**
[day-by-day list with times]

**Suggested time blocks:**
| Day | Block | Project/Focus |
|-----|-------|---------------|
| Mon | 9–11 AM | [project] |
...

**Flags:**
- [Any day with no focus time]
- [Any project with no scheduled time]
- [Wednesday = office day]
```

Be direct about conflicts. If the calendar is too full to make progress on the ONE Big Thing, say so.
