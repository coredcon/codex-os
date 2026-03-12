# Codex.os

A personal operating system for Claude Code, built on top of an Obsidian vault.

Codex.os turns Claude Code into a persistent thinking partner — **Vox** — that knows your projects, your life context, and your weekly rhythm. It uses an Obsidian vault as a second brain and wraps it with a layer of session protocols, hooks, and scripts that make Claude feel like a continuous presence rather than a stateless tool.

---

## What's in this repo

This is a **sanitized template** of the full system. All personal data has been removed. The structure, scripts, hooks, and protocols are complete and functional.

```
codex-os/
├── CLAUDE.md                    # Main system prompt — Vox's brain
├── VAULT-INDEX.md               # Live dashboard — Vox reads this every session
├── .claude/
│   ├── settings.json            # Hook configuration for Claude Code
│   ├── WORKING.md               # Mid-session crash buffer
│   ├── pending-reflection.md    # File change queue (written by VoxWatcher)
│   ├── state.md                 # Current pressures, momentum, open loops
│   ├── session-brief.md         # Pre-digested startup cache (generated nightly)
│   ├── routing-policy.md        # When to use Haiku vs Sonnet
│   ├── initiative-rules.md      # When Vox proactively surfaces things
│   ├── agents/
│   │   └── vox-core.md          # Vox persona — loaded for deep sessions
│   ├── hooks/
│   │   ├── protect-archive.sh   # Blocks writes to 07 Archive/
│   │   ├── auto-commit.sh       # Auto-commits vault after every file write
│   │   ├── run-session-init.bat # Windows launcher for session-init hook
│   │   └── session-init.sh      # Session banner + familiar state bridge
│   ├── scripts/
│   │   └── vox-overnight.py     # Nightly script: pre-creates daily note + session brief
│   ├── vox-watcher/
│   │   ├── vox-watcher.py       # System tray watcher — logs vault changes for Vox
│   │   └── config.json          # VoxWatcher config
│   └── config/
│       ├── freshdesk.env.example
│       ├── govee.env.example
│       └── familiar.env.example
├── Templates/
│   ├── Daily-Note.md
│   ├── Weekly-Review.md
│   ├── Project.md
│   ├── Meeting.md
│   ├── Vibe-Coding-Project.md
│   ├── Home-Project.md
│   ├── TTRPG-Session-Bridge.md
│   └── 3D-Print-Job.md
└── [vault folders] 00-07         # Empty scaffolding with .gitkeep
```

---

## How it works

### The Core Idea

Claude Code runs inside your Obsidian vault. `CLAUDE.md` (Claude's project instructions file) defines Vox — a persistent assistant persona that knows your vault layout, your life context, and how you work. Every session, Vox follows a startup protocol to reload context and pick up where you left off.

### Session Flow

1. **Hook fires** — `session-init.sh` runs on every prompt. It checks if this is the first prompt of the session and displays a status banner (date, daily note status, inbox count, ONE Big Thing).
2. **Vox starts up** — reads `.claude/WORKING.md` for crash recovery, `.claude/pending-reflection.md` for file changes since last session, then either reads a pre-generated `session-brief.md` or falls back to reading source files directly.
3. **Calendar pull** — live Google Calendar check via MCP (not from brief — always fresh).
4. **Get to work** — Vox surfaces the ONE Big Thing for the week and asks what you're working on.
5. **Mid-session** — `auto-commit.sh` hook fires after every file write, keeping the vault version-controlled. Vox writes key moments to `WORKING.md` as crash insurance.
6. **Session end** — Vox writes a `## Vox Session Digest` block to the daily note, updates `state.md`, and clears `WORKING.md`.

### Overnight Prep

`vox-overnight.py` runs nightly via Task Scheduler (~5 AM). It:
- Pre-creates tomorrow's daily note from the template, carrying forward unchecked tasks
- Parses your work calendar ICS for tomorrow's events
- Pulls project statuses from `VAULT-INDEX.md`
- Fetches open support tickets (if Freshdesk is configured)
- Writes `.claude/session-brief.md` — a single pre-digested file Vox reads at startup instead of 8+ sources

### VoxWatcher

A Python system tray app that watches the vault for file changes while Claude isn't running. When files are created or modified (including by Obsidian mobile sync), it logs them to `pending-reflection.md` and triggers a QMD re-index. Vox processes this queue at session start.

### Token Efficiency (Routing Policy)

See `.claude/routing-policy.md`. The short version: Sonnet handles anything requiring judgment; Haiku handles mechanical tasks (file writes, simple lookups, formatting). This is ~20x cheaper for routine operations.

---

## Setup

### Prerequisites

- [Claude Code](https://claude.ai/code) (the CLI)
- [Obsidian](https://obsidian.md) (the vault UI — optional but recommended)
- Git (for auto-commit hook)
- Python 3.10+ (for overnight script and session-init)
- [QMD](https://github.com/tobilu/qmd) — local semantic search over your vault (optional but powerful)

### Quick Start

1. **Clone or fork this repo** into your Obsidian vault root (or copy the files in)
2. **Edit `CLAUDE.md`** — fill in all `[bracket]` placeholders with your own info
3. **Edit `vox-core.md`** — customize the Vox persona for your own life context
4. **Update paths** in `settings.json`, `auto-commit.sh`, `run-session-init.bat`, `session-init.sh`, and `vox-overnight.py` to point to your vault
5. **Set up hooks** — Claude Code will pick up `.claude/settings.json` automatically
6. **Schedule the overnight script** via Task Scheduler (Windows) or cron (Linux/Mac)
7. **Run VoxWatcher** at startup if you want file-change tracking between sessions

### MCP Servers

The included `.mcp.json` connects to QMD (local semantic search). You can also add Google Calendar and Gmail MCP servers for live calendar pulls at startup — see [Claude MCP docs](https://docs.anthropic.com/claude/mcp) for setup.

---

## Customization

### Making Vox Yours

`CLAUDE.md` is Vox's brain. The most important sections to customize:
- **Identity** — your name, timezone, work situation
- **Vault Map** — adjust if you rename folders
- **Session Protocol** — add or remove startup steps
- **Active Context** — your current ONE Big Thing

`vox-core.md` is the deeper persona file — loaded via the `agents/` system for richer sessions. Customize:
- What Vox knows about you (personality, health considerations, how you communicate)
- What projects are active
- Any specialized modes (e.g., a "Campaign Mode" if you run TTRPGs)

### Modifying Folders

The 8-folder structure (00 Inbox through 07 Archive) is a convention, not a requirement. If you rename folders, update:
- `CLAUDE.md` Vault Map
- `protect-archive.sh` (the archive folder name)
- `session-init.sh` (inbox count path)

### Integrations

- **Freshdesk** — configure `config/freshdesk.env` to pull open tickets into the nightly brief
- **Govee lights** — configure `config/govee.env` for ambient lighting that responds to Vox session state
- **Desktop Familiar** — a separate Raspberry Pi + Llama project for ambient AI presence; `session-init.sh` pulls its state on every prompt

---

## Philosophy

This system was built around one idea: **Claude should feel like it never left**.

The overnight script, the session brief, the WORKING.md crash buffer, the VoxWatcher file change queue — all of it exists to minimize the "re-explain everything" tax at the start of each conversation. The goal is to open Claude Code and immediately be in context, not spend 5 minutes re-establishing it.

The other idea: **your life system should have opinions**. `initiative-rules.md` defines when Vox speaks up without being asked. The routing policy defines how to not waste tokens on mechanical work. The 3-task limit enforces focus. These aren't just instructions — they're a collaboration protocol.

---

## Related

- [Claude Code docs](https://docs.anthropic.com/claude/claude-code)
- [QMD — local semantic search](https://github.com/tobilu/qmd)
- [Obsidian](https://obsidian.md)
