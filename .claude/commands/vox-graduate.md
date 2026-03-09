# /graduate — Promote Ideas from Daily Notes

Scan recent daily notes for half-formed ideas that deserve their own note. Promote them.

## Steps

1. Get today's date
2. Scan all daily notes from the past 14 days (`01 Daily/YYYY/MM/`)
3. Look for:
   - Ideas marked with `#idea`, `💡`, or `- [ ] explore:`
   - Recurring topics that appear in multiple days
   - Questions the user asked themselves
   - Anything phrased as "I should...", "what if...", "look into..."
   - Concepts that got more than one sentence of development
4. For each candidate, summarize: what is it, when did it appear, how many times
5. Ask which ones to promote (or promote all if instructed)
6. For each promoted idea, create a note in the appropriate folder:
   - Work idea → `03 Projects/Work/`
   - Creative/code idea → `03 Projects/Vibe-Coding/` or `06 Resources/`
   - Personal/life idea → `05 Areas/` or `06 Resources/Personal/`
   - Unclear → `00 Inbox/`
7. Each promoted note uses the basic structure: title, source (date + daily note link), core idea, open questions, related notes

## Output

List what was found, what was promoted, and where each went. Flag anything that appeared 3+ times as high-signal.

Best run during weekly review alongside `/schedule`.
