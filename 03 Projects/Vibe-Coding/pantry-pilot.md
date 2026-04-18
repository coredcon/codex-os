---
date: 2026-04-18
status: Idea — not started
last_updated: 2026-04-18
stack: TBD (web service likely)
tags: [vibe-coding, project, idea, household, saas]
---

# Pantry Pilot

## The Idea (one sentence)
A passive household replenishment tool that reads your grocery email receipts and Amazon order history to automatically generate your next shopping list — no forms, no manual input.

## What problem does it solve?
Every household struggles with bi-weekly grocery and household item decisions — what's running low, what got wasted, what to reorder. Existing apps require active maintenance (lists, forms, photos) which no one sustains. This watches the data you already generate and does the work for you.

## Core Insight
**No one will fill out forms or take pictures.** The only solution that works long-term is one that requires zero behavior change — it plugs into data flows that already exist.

## Data Sources
- **Gmail OAuth** — parse email receipts from Kroger, Walmart, Target, Costco, any store that sends itemized receipts
- **Amazon order history** — covers Fresh, Pantry, Subscribe & Save, and all household goods
- **Subscribe & Save optimization** — manage timing based on actual consumption, not guesses

## How It Works
1. User connects Gmail + Amazon once (OAuth)
2. App reads purchase history, builds household consumption model over time
3. Surfaces pre-built shopping list before the next trip — "you're probably out of milk, eggs, and paper towels"
4. Optional: weekly email digest (no app install required)
5. Gets smarter with every receipt

## Monetization
- Free tier: one email account, basic list generation
- Pro ($4-8/month): multiple family members, multiple email accounts, Amazon integration, Subscribe & Save management
- SaaS model — recurring, not one-time

## Market
- Universal problem — every household has this pain
- Not a nerd product — mainstream audience
- No zero-input competitor exists (all current apps require manual maintenance)

## Tech Considerations
- Gmail API (OAuth) — legitimate, well-documented
- Amazon: order history via email receipt parsing (no official API for consumer purchase history)
- Kroger/grocery APIs: don't expose purchase history — email is the only clean path
- Could live as web service + weekly email digest (lower friction than an app install)

## What I Learned / Market Research
- Kroger has a developer API but purchase history is deliberately excluded
- No Plaid-equivalent exists for grocery loyalty data
- Email receipt parsing is store-agnostic and legally clean
- TouchPortal (niche desktop tool) made millions — mainstream household tool has larger TAM
- Potential $4-8/mo SaaS with low churn (household staples = high retention)

## Next Steps (when ready to build)
- [ ] Test Gmail API receipt parsing on real Kroger/Kroger emails
- [ ] Map Amazon order history email format
- [ ] Define MVP: connect Gmail → parse 3 months of receipts → generate first list
- [ ] Validate with Leslie and kids — would they actually use the output?

---

## Dev Log

### 2026-04-18 — Idea Captured
Brainstormed during late-night HookSnap + Canonex session. Came out of "what would I build to retire on" conversation. Core insight: passive observation beats active input every time. Saved for future vibe coding session.
