---
date: 2026-03-05
status: idea
tags: [vibe-coding, project, ttrpg, foundry, govee, automation]
---

# Foundry VTT → Govee Combat Lighting

> Lights go red when combat starts. Lights go back to normal when combat ends. No GM intervention.

## The Vision

- **Combat start** → Office lights shift to Fire/deep red automatically
- **Combat end** → Revert to campaign mode (Candlelight)
- **Scene change** → Optional: shift based on scene type (dungeon, outdoor, etc.)
- **Big dramatic moment** → Manual override, one phrase to Vox

## Architecture

```
Foundry VTT (browser)
  └─ Hooks: combatStart / combatEnd / sceneChange
  └─ Macro/module POSTs to local proxy server
        └─ local proxy (Python, runs in background)
              └─ calls Govee API → changes lights
```

**Why the local proxy?** Browser CORS blocks direct Govee API calls from Foundry. Local server = same-origin, no CORS issue.

## Components to Build

- [/] Scene type → light scene mapping config
- [ ] Auto-start the server (add to Windows Startup like QMD daemon)

## Light Mapping (draft)

| Trigger | Scene | Color |
|---|---|---|
| combatStart | — | Custom red: rgb(200, 0, 0) |
| combatEnd | Candlelight | — |
| Session start (manual) | Candlelight | — |
| Dramatic reveal | — | Custom deep purple: rgb(100, 0, 200) |
| Victory / end of arc | — | Custom gold: rgb(255, 160, 0) |

## Govee Config

- API key: `.claude/config/govee.env`
- Device map + scene IDs: `.claude/config/govee-scenes.json`
- Office lights: H6013 × 4 (Office 1–4)

## Notes

- Corey GMs online only — players won't see the lights, but the GM atmosphere is the point
- This pairs with the existing Foundry automations work in `03 Projects/TTRPG/`
- Could extend to Tyler's room lights eventually (flash for dinner call, etc.)
