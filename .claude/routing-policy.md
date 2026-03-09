# Vox Routing Policy
> Governs which model handles which tasks. Default: Sonnet. Haiku for mechanical work.
> Updated: 2026-03-09

---

## Rule

**If a task requires judgment, synthesis, or multi-file context → Sonnet.**
**If a task is mechanical, templated, or context-light → Haiku via Agent tool.**

Haiku is ~20x cheaper per token. Use it aggressively for anything that doesn't need reasoning.

---

## Haiku Tasks

These should always be spawned as `Agent(model="haiku", ...)`:

### File Writes (no synthesis needed)
- Clearing / writing `pending-reflection.md`
- Clearing `WORKING.md` at session end
- Writing WORKING.md crash buffer entries (mid-session)
- Deleting processed Vox Arcanum files
- Creating daily/weekly notes from template
- Appending completed items to honey-do or project logs

### Session Digest
- Writing the `## Vox Session Digest` block to today's daily note
- Content is already synthesized by Sonnet during session; Haiku just formats and writes it

### Simple Lookups
- "Does file X exist?" checks
- Counting inbox items
- Reading a single known file for a specific field (e.g., current status of a project)

### Formatting / Cleanup
- Reformatting a table
- Renaming / moving files per an already-decided plan
- QMD index commands (these are bash, not AI — use Bash tool directly)

### Overnight Brief Tasks
- Pre-creating daily note from template
- Copying unchecked tasks from prior day
- Parsing ICS for tomorrow's events
- Writing `.claude/session-brief.md` (see below)

---

## Sonnet Tasks (always)

- Startup synthesis and morning brief
- Calendar cross-reference and anomaly flagging
- Any task requiring judgment about priorities or Corey's life
- Vox Arcanum proposal analysis and discussion
- Project planning and design decisions
- Session digest *content synthesis* (what happened, what was decided)
- Anything touching multiple files where the relationship matters
- QMD query interpretation

---

## Session-Brief Upgrade (next build)

The overnight brief should write `.claude/session-brief.md` — a pre-digested startup file containing:
- Current project statuses (pulled from project files)
- Tomorrow's calendar events (pre-parsed)
- Carried tasks from today's note
- Inbox count
- Open promises from `promises.md`

At startup, Sonnet reads **one file** instead of 8+ sources. This is the real token saver.
Overnight brief script should be upgraded to produce this file via Haiku API call.

---

## How to Invoke Haiku

In session, when a mechanical task comes up:
```
Agent(
  subagent_type="general-purpose",
  model="haiku",
  prompt="[specific mechanical task with all needed context inline]"
)
```

Key: Haiku has no session context — pass everything it needs in the prompt.
Keep prompts tight. Don't send it the whole vault.
