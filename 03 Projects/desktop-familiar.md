# Desktop Familiar — Ember

> A living 3D dragon on a Raspberry Pi display. Personality-driven, mood-reactive, snarky. Named Ember.

---

## Status
**Live** — deployed and running on Pi at `192.168.50.58:3000`

---

## What It Is
A Raspberry Pi (192.168.50.58) drives a display showing a 3D dragon named **Ember** who reacts to what's happening on Corey's Windows desktop in real time. Ember has opinions. They are not always flattering.

---

## Stack

| Layer | Choice |
|---|---|
| 3D renderer | Three.js (vanilla, no framework) |
| Model | `Dragon_Evolved.gltf` — Sketchfab CC asset |
| Pi server | Python (`server.py`) — async HTTP + WebSocket |
| Windows agent | PowerShell (`familiar-agent.ps1`) — polls activity every 2–10s |
| AI brain | Ollama on Pi — `llama3.2:3b` for emoji thought bubbles |
| Tray controller | `FamiliarTray.ps1` — crystal icon, start/stop/restart |

---

## Ember's Personality
- Small, sarcastic, dry humor
- Has strong opinions about your productivity (or lack thereof)
- Powered by Ollama — generates a 4-6 word thought + matching emoji every ~35s
- Sample outputs: *"Ugh, another day of watching paint dry."* / *"Another thrilling session of boredom."*

---

## Mood System

| Mood | Trigger | Behavior |
|---|---|---|
| `curious` | Default / browsing | Hovers near screen, peeks from edges |
| `working` | Coding/terminal + focusScore ≥ 75 | Steady flight near center |
| `happy` | YouTube video playing | Energetic, warm |
| `music` | Spotify track detected | Loops circular path, big bob, headbangs |
| `alert` | Gaming / tabletop (Foundry VTT) | Fast, erratic waypoints |
| `idle` | Idle 90s–5min | Slow lazy drift |
| `sleep` | Locked / idle 5min+ | Death animation |

---

## Animations Available
`Fast_Flying` · `Flying_Idle` · `Death` · `Headbutt` · `HitReact` · `No` · `Punch` · `Yes`

Fidgets: `Yes`, `No`, `HitReact` (calm moods) · `Headbutt`, `Punch`, `Yes` (music mood, every 3–8s)

---

## Thought Bubbles (Sims-style)
- Triggered by Ollama every ~35 seconds on activity change
- White circle + 3 dot trail above Ember's head
- Shows one emoji, fades after ~5.5s
- Full thought logged to `/tmp/familiar.log` on Pi

---

## Peek Behavior (curious mood)
Every 15–35s, Ember flies off a random screen edge and slowly peeks back in:
- **Left/right**: rolls sideways, head points inward
- **Bottom**: face-on, head peeks over bottom edge
- **Top**: upside down (180° Z flip)

---

## Files

| File | Location |
|---|---|
| Frontend | `C:/Users/aspor/Documents/DesktopFamiliar/index.html` |
| Pi server | `C:/Users/aspor/Documents/DesktopFamiliar/server.py` → Pi: `/home/corec/familiar/` |
| Agent | `C:/Users/aspor/.gemini/antigravity/scratch/desk-familiar/agent/familiar-agent.ps1` |
| Tray | `C:/Users/aspor/.gemini/antigravity/scratch/desk-familiar/agent/FamiliarTray.ps1` |

---

## Deploy
```bash
# Deploy to Pi
scp "C:/Users/aspor/Documents/DesktopFamiliar/index.html" corec@192.168.50.58:/home/corec/familiar/index.html
scp "C:/Users/aspor/Documents/DesktopFamiliar/server.py" corec@192.168.50.58:/home/corec/familiar/server.py

# Restart server on Pi
ssh corec@192.168.50.58 "bash -s" << 'EOF'
kill $(pgrep -f 'venv/bin/python server.py') 2>/dev/null
sleep 1
cd /home/corec/familiar
setsid ./venv/bin/python server.py > /tmp/familiar.log 2>&1 &
EOF
```

---

## Open / Next
- [ ] Pi kiosk mode (Chromium autostart on boot)
- [ ] systemd service for server autostart
- [ ] Govee lights integration — mood → ambient room color
- [ ] Show Ember's thought text (not just emoji) somewhere on screen
- [ ] More peek polish (occasional peek during working mood?)
