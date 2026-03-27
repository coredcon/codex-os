---
title: Vox Workspace
status: Active — Daily Use
started: 2026-03-14
last_updated: 2026-03-26
tags: [vibe-coding, electron, vox, tooling]
---

# Vox Workspace

A local Electron app that wraps the Claude Code / Vox terminal session in a richer, reactive UI — split-pane layout with Vox on the left and live, file-backed panels on the right.

---

## The Core Idea

The terminal isn't going away — it's getting a frame. The left side is the actual Claude Code process running inside an embedded terminal (xterm.js). The right side is a panel system that **reacts to files Vox writes**. When Vox updates a task, the board flips. When Vox edits a vault file, the viewer re-renders. No magic plumbing needed — just a file watcher and a reactive UI.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Electron App                      │
│                                                     │
│  Main Process                                       │
│  ├── Spawns: claude (Claude Code subprocess)        │
│  ├── Spawns: node-pty (PTY for xterm.js)            │
│  ├── Runs:   chokidar (vault file watcher)          │
│  └── IPC:    bridges subprocess ↔ renderer          │
│                                                     │
│  Renderer (React + Vite)                            │
│  ├── Left:  xterm.js terminal (Vox session)         │
│  └── Right: Panel system (swappable views)          │
└─────────────────────────────────────────────────────┘
```

**Key principle:** Vox writes files → chokidar detects change → IPC push to renderer → panel re-renders. Vox doesn't need to know the app exists. The panels are just smart file readers.

**Critical:** Claude Code must be spawned with `cwd` set to `F:\My Drive\Obsidian\Codex.os`. This is what makes it Vox — not a generic Claude Code instance. CLAUDE.md, all hooks, and the `.claude/` config load automatically from the working directory. The app replaces `Codex_os.bat` entirely; it doesn't run alongside it.

---

## Tech Stack

| Layer | Choice | Why |
|---|---|---|
| Shell | **Electron** | File system access, child processes, no browser sandbox restrictions |
| Bundler | **Vite** | Fast, modern, great Electron support |
| UI | **React** | Component-based, huge ecosystem, good for panels |
| Terminal | **xterm.js + node-pty** | What VS Code uses — proper ANSI, colors, cursor support |
| File watching | **chokidar** | Battle-tested, cross-platform, efficient |
| Markdown | **react-markdown + remark-gfm** | Clean MD rendering with GFM support |
| Charts | **Recharts** | React-native, composable, looks good |
| Styling | **Tailwind CSS** | Utility-first, fast to iterate on, clean dark mode |

---

## Panel System — Phase 1 (Ship These First)

### 1. Vault File Viewer
- File tree of the Codex.os vault
- Click any file → renders as markdown in the panel
- Watches for changes — if Vox edits the file mid-session, it live-updates
- Search/filter by filename

### 2. Kanban Board
- Reads task status from vault markdown files (frontmatter or task lists)
- Columns: Backlog / In Progress / Done (or per-project)
- Vox can write task status changes and the card moves in real time
- Click a card → expand to see the full file context

### 3. Today View
- Reads today's daily note and renders it cleanly
- Shows the Top 3 tasks, log, morning check-in
- Watches for changes — as Vox writes to it during session, it updates live
- Simple, always-visible anchor for the day

---

## Panel System — Phase 2 (Later)

| Panel | What it does |
|---|---|
| **Govee Controls** | Mood buttons that call `familiar-mood.py` — click to switch lighting |
| **Calendar** | Pulls Google Calendar via the existing MCP; visual day/week view |
| **Project Dashboard** | VAULT-INDEX-style status board — active projects, last touched, next action |
| **Chart View** | Vox generates data → writes JSON → panel renders as chart (bar, line, pie) |
| **Campaign Panel** | EotFG-specific — zone map, encounter tracker, NPC quick-reference |

---

## Vox's Opinion: What to Watch Out For

**node-pty on Windows is finicky.** It works, but Windows PTY support has edge cases. Budget time to get the terminal feeling right — ANSI colors, resize behavior, scrollback. VS Code solved this, so their solution is the reference.

**Don't over-build panels before you know what's actually useful.** The Kanban sounds great in theory. The real test is whether you actually use it during a session. Ship terminal + vault viewer first. Add panels only when you feel the absence of one.

**Electron apps bloat fast.** Keep the dependency list short. Resist the urge to add things "just in case." The app should feel snappy — if it starts feeling heavy, something went wrong.

**File-backed is the right philosophy.** Resist the temptation to build a database or a custom data format. Everything should be readable as a plain text file without the app. Vault-first, always.

**The terminal has to be first-class.** If xterm.js doesn't feel as good as the real terminal, nobody will use this. Get that right before touching the panels.

---

## MVP Definition

> The app is "done enough to use daily" when:
> - xterm.js terminal running Claude Code feels identical to the standalone terminal
> - Vault file viewer opens and live-updates correctly
> - Today view shows the daily note and refreshes when Vox edits it
> - Kanban shows active project tasks and responds to Vox writes
> - App launches via the same shortcut as the current `Codex_os.bat`

---

## Open Questions

- **Electron vs. browser-only?** Electron gives file system + subprocess access without a local server. A browser app needs a Node.js backend server running separately. Electron is the cleaner single-package solution.
- **Panel layout:** Fixed split (50/50) or resizable drag handle? Resizable is better but adds complexity.
- **Tab system for panels:** Multiple panels accessible via tabs on the right? Or single-panel with a switcher?
- **Mobile?** If Tailscale is set up, the renderer could theoretically be served to a phone browser — but the subprocess/file-watcher stays on PC. Worth exploring after MVP.

---

## Project Status

### Core Infrastructure ✅
- [x] Scaffold Electron + Vite + React + TypeScript
- [x] xterm.js + node-pty terminal emulation
- [x] Claude Code subprocess piped into terminal
- [x] chokidar file watcher + IPC to renderer
- [x] Remote control auto-spawn (Claude mobile access)
- [x] Design system overhaul — 4-level surface tokens, unified Cascadia Code font
- [x] App launcher via `Vox Workspace.vbs` (desktop shortcut, replaces Codex_os.bat)

### Mode System ✅ (6 modes)
- [x] **Daily** — Today, Vault, Board, Lights
- [x] **Work** — Queue (Freshdesk), Calendar, Board, Docs
- [x] **Builder** — Projects, Board, Rabbit Holes, Vault, Lights
- [x] **Home** — Nest (HomePanel), Honey-Do, Projects, Health (amber theme)
- [x] **Career** — Jobs (job-tracker.md), Overview, Files
- [x] **Campaign** — EotFG vault, Session Notes (placeholder), Encounter Ref (placeholder)

### Panels Built ✅
- [x] TodayPanel — daily note, tasks, Focus card, **Best Next Action intelligence card**
- [x] VaultPanel — file tree + markdown preview + edit mode + Discuss with Vox (right-click)
- [x] KanbanPanel — 3-column drag & drop, project cards, subtasks, manual task entry
- [x] FreshdeskPanel — live ticket queue, change detection (diffs updated_at/status), badge counts, filter pills
- [x] GoveePanel — mood setter via direct Govee API
- [x] ProjectsPanel — master-detail, category auto-discovery, tasks + notes + dev log
- [x] HomePanel — honey-do tasks, ambient context widget, family card, house projects
- [x] WorkCalendarPanel — 7-day ICS reader (node-ical), NOW badge, recurring events

### Intelligence Layer ✅
- [x] Best Next Action card — 5-state rules engine (urgent/important/quick-win/recovery/clear)
- [ ] Priority tagging on individual tasks (avoidance/blocked/emotionally heavy)
- [ ] Mode-aware proactive Vox surface in panel layer

### Pending
- [ ] Campaign panels: Session Notes + Encounter Reference (still PlaceholderPanel)
- [ ] Focus Mode: minimal UI, single task large, optional timer
- [ ] Quick Capture widget → 00 Inbox/
- [ ] Persist split pane % to localStorage
- [ ] Rabbit Holes panel: needs UI/design pass
- [ ] FreshdeskPanel / ProjectsPanel / RabbitHolePanel CSS: still have hardcoded hex
- [ ] Requester name on tickets (needs per-ticket API calls)

---

## Phase 2 — Command Nexus Vision
> Captured 2026-03-14 from Corey + ChatGPT proposal, with Vox analysis

### Core Design Principle
**Every feature must serve:** `Recover context → take action → preserve state`

### Vox's Recommended Build Sequence

**1. State strip** (highest ROI, ~2 hrs)
- Reads `.claude/state.md` directly — data already exists
- Shows: Active Mode | ONE Big Thing | Open Loop count | Context count
- Makes the app feel like it has a brain

**2. Today: Focus card at top** (~1 hr)
- Pulls ONE Big Thing + Current Mode from state.md into a prominent card
- Replaces the blank top of the Today panel

**3. Vault: File actions** (~2–3 hrs)
- "Open externally" — trivial (shell.openExternal)
- "Pin to context" — writes to `.claude/CONTEXT.md`, Vox reads it
- "Send to terminal" — pastes formatted command directly into PTY

**4. Board: Task detail pane** (~2 hrs)
- Click a card → expand to show description, project, notes, next action
- Currently cards show text only

**5+ Later:** Cross-linking, Workspace Modes (Builder/GM/Archivist/etc.), Decision Logging, Session Continuity panel

### Architecture Notes
- **Pinned Context mechanism:** Electron app writes `.claude/CONTEXT.md` → Vox reads it at session start. Don't invent new infrastructure — go through the filesystem.
- **"Summarize with Vox" / terminal actions:** Paste formatted command into PTY directly. Clean, honest, no fake telepathy.
- **State strip data source:** `.claude/state.md` — already maintained every session. Don't duplicate.
- **Session continuity data:** Already exists in session-brief.md + WORKING.md. Surface it, don't rebuild it.

### What to Avoid
- Adding tabs before current 4 are deep
- Turning Vault into an Obsidian clone
- Features that act silently without user intent
- Building 80% of 10 things instead of 100% of 3
