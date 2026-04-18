---
date: 2026-03-03
status: Beta shipped — awaiting feedback
last_updated: 2026-03-26
stack: Electron, React, CRA
tags: [vibe-coding, project, ttrpg]
---

# Canonex

## The Idea (one sentence)
A standalone local application that serves as a digital GM screen for TTRPG sessions.

## What problem does it solve?
Centralizes GM reference material, rules lookup, and session tools in one place — replaces physical GM screens and scattered tabs.

## Tech Stack

## Links
- Repo:
- Live:
- Working dir: `C:\Users\aspor\Documents\Canonex`

---

## Dev Log

### 2026-03-06 — v0.1.5 — Beta fixes from Nick's feedback
- `perMachine: false` — installs to `%LOCALAPPDATA%`, no admin required; fixes text box input issue
- Shop dropdown: replaced native `<select>` with Radix `Select` — fully theme-aware, no OS color clash
- Portrait AI generation removed (Pollinations was unreliable); replaced with upload-only flow in NPCNew + NPCDetail
- Removed `generate-portrait` IPC handler from electron.js

### 2026-03-06 — Full cleanup + size optimization + ready for beta
- Ripped out Python backend entirely — all three endpoints (generate-npc, generate-shop, generate-portrait) ported to Electron IPC handlers in electron.js
- Data files (names/traits/backgrounds/items JSON) copied to `frontend/public/data/` — bundled into asar via CRA build
- Removed express, cors, axios — replaced with Node built-in `http` module + `fetch()` (Electron/Node 18+)
- This eliminated `call-bind-apply-helpers` at the source — no more pruning fights
- Enabled `asar: true` — install went from crawl to fast
- Fixed blank screen: `BrowserRouter` → `HashRouter` (pushState doesn't work on file:// protocol)
- Fixed exit error: `killPythonBackend` reference left in `window-all-closed` handler — removed
- **Size reduction:** Moved all packages from `dependencies` → `devDependencies` — electron-builder only bundles `dependencies` into asar; since main process uses zero npm packages (all renderer deps webpack-compiled), nothing belongs there
  - asar: 274 MB → 9.6 MB
  - Installer: ~109 MB → 80 MB
  - Installed size: 541 MB → 278 MB (floor is Electron runtime — unavoidable)
- **Result: App launches clean, renders correctly, exits clean, ships lean**
- Next: send to Nick for beta testing

### 2026-03-05 — Installer debugging
- Installer works (asar:false, perMachine NSIS) but `call-bind-apply-helpers` was missing from installed node_modules
- Root cause: electron-builder's dependency graph pruning drops transitive deps it can't trace
- Fix applied: added `require('call-bind-apply-helpers')` explicitly in `electron.js` to force inclusion

### 2026-03-03 — Session 1
> Project added to vault.

---

## Current Status
Beta shipped 2026-03-06. Nick has the installer. Collecting feedback from PF2e party Discord. World Simulation built but test run still pending.

## Features Built
- NPC generator (name/traits/backgrounds, local JSON data)
- Shop generator
- Portrait: upload-only (AI generation removed — Pollinations was unreliable)
- Installer: 80MB, no admin required (`perMachine: false`)
- **World Simulation** — `/simulation` endpoint; `npm start` in frontend + backend restart to run test

## Decisions Made

## What I Learned

## Beta Testers
- Nick (friend, coworker, PF2e player) — first candidate

## Ideas / Next Features
- **Bestiary** — separate from NPC list; preload ORC-licensed stat blocks from AoN (text only, no artwork); feeds encounter/initiative tool
- **Counteract Calculator** — inputs: counteract level + degree of success + target level → clear yes/no result
- **Portrait: drop AI generation** — replace with upload-your-own; local models (SD) are 2-4GB, non-starter for a GM screen app

---

## Beta Feedback Log

### 2026-03-06 — Nick (Round 1)

**Bugs**
- Must run as Admin to enter text in text boxes — likely a file system permissions issue with the install location
- Generate Portrait (NPC) is broken — free AI endpoint not reliable; may need to reconsider approach
- Shop screen dropdown is hard to read on some themes — contrast issue

**Feature Requests**
- Bestiary separate from NPC list — makes encounter/initiative tracking cleaner
- Counteract calculator
