# /closeday — End of Day Capture

Close out the day by logging what happened and setting up tomorrow.

## Steps

1. Get today's date
2. Read today's daily note (`01 Daily/YYYY/MM/YYYY-MM-DD.md`)
3. Read `VAULT-INDEX.md` for active projects and ONE Big Thing
4. Ask: "What did you get done today? Anything to capture before we close out?"
5. Wait for response, then:
   - Log completed items to today's daily note
   - Identify anything unfinished that should carry to tomorrow
   - Surface any new ideas or captures that should go to `00 Inbox/`
6. Check personal Google Calendar for tomorrow's events
7. Parse `06 Resources/Work/work-calendar.ics` for tomorrow's work meetings
8. Write a "Tomorrow" section to today's daily note with:
   - ONE Thing for tomorrow
   - Known meetings
   - Max 2 carry-over tasks

## Output format

```
## Day closed — [Date]

**Done today:** [list]
**Captured to inbox:** [any new items]
**Carry-overs:** [unfinished]

---
**Tomorrow: [Day], [Date]**
- ONE Thing: [suggested based on projects + priorities]
- Meetings: [from calendars]
- Also: [max 2 carry-overs]
```

End with: "Vault updated. See you tomorrow."
