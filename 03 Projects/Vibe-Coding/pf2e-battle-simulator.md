---
title: PF2e Battle Simulator
status: idea
tags: [vibe-coding, pf2e, ttrpg, tools]
created: 2026-04-16
---

# PF2e Battle Simulator

## The Idea
Drop in party characters and creatures, have AI run multiple combat simulations, get a statistical report. Useful for encounter balance testing before running sessions.

## Core Loop
1. Parse character + creature stat blocks (JSON input)
2. Simulate rounds: each combatant picks actions based on simple AI heuristics
3. Track HP, spell slots, conditions, action economy across the round
4. Run N iterations (100+)
5. Output report

## Report Output
- Average rounds to resolve
- TPK rate (%)
- Average party HP remaining at end
- Resource burn per wave (spell slots, hero points, big heals)
- "Danger spike" rounds — when did the party come closest to wiping?

## AI Decision Brain Options
**Option A — Hardcoded heuristics (fast, no API cost)**
- Martials: Strike with best attack unless target has resistance → switch damage type
- Casters: Use highest available spell slot on priority target; fallback to cantrips
- Boss creatures: Lead with signature ability (gaze, aura, special attack), then strikes
- Healing: auto-trigger if party member below 30% HP

**Option B — Claude API decision layer (smarter, costs tokens)**
- Each turn: feed current battle state to Claude Haiku, ask "what's the optimal action?"
- Slower, more expensive, but handles edge cases and unusual abilities
- Better for narrative playtests, worse for bulk simulation runs

Probably: Option A for bulk runs, Option B for single "narrative mode" simulation.

## Stack
- Python, no framework needed
- JSON stat block schema (define once, reuse for all PF2e creatures/characters)
- Simple CLI: `python simulate.py --party party.json --encounter encounter.json --runs 100`
- Output to terminal or markdown report file

## Why PF2e Works Well
- Tight, predictable math — scaling is linear and consistent
- Action economy is simple (3 actions, each action has a clear cost)
- Conditions (frightened, stunned, etc.) have numeric values, easy to track
- XP budget system already validates encounter difficulty — simulator confirms it empirically

## Triggered By
Night Attack S1 encounter for EotFG — needed to verify 3-wave sequential encounter (Resonance Shades → Shattered Hounds → Broken Warden) was survivable for L11 party with enough resources to reach Fex at 30% HP for the monologue beat.

## Next Steps (when ready to build)
- [ ] Define JSON schema for character and creature stat blocks
- [ ] Build round simulator with heuristic AI
- [ ] Test against Night Attack S1 as first real use case
- [ ] Add multi-wave support (resources carry across waves)
