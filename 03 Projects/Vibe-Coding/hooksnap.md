---
title: HookSnap
status: In Progress
started: 2026-04-02
last_updated: 2026-04-03
tags: [vibe-coding, mobile, android, webhook, saas]
---

# HookSnap — Webhook Proxy + Inspector

## What It Is
A permanent webhook proxy with a mobile-first inspector. You point your webhook source at a HookSnap URL once — it forwards to your real endpoint (so production never breaks) AND logs every payload so you can inspect, diff, and replay it on your phone.

**The key differentiator:** Not a temp debugging URL. Always-on forwarding proxy with mobile push notifications when traffic hits.

## Why It's Interesting
- No mobile-native competitor exists. Everything is web-only (Webhook.site, Webhook Rodeo, RequestBin).
- Target users: integration engineers, TAMs, solutions engineers, developers building with Stripe/GitHub/Shopify webhooks — people who debug webhooks for a living.
- Mobile push notifications when a payload fires = genuinely useful for support/TAM on a call with a customer.

## How It Works

```
Webhook source (POS, Stripe, etc.)
        ↓
hooksnap.app/h/[slug]   ← your permanent URL (change once)
        ↓           ↓
  [logged]     [forwarded to real endpoint — production still works]
        ↓
  Mobile app ← push notification fires
```

## Tech Stack
| Layer | Tool | Cost |
|---|---|---|
| Mobile | Expo + React Native (Android-first) | Free |
| Backend | Next.js + TypeScript | Free |
| Hosting | Vercel (Hobby plan) | Free/$7 |
| Storage | Upstash Redis | Free tier |
| Subscriptions | RevenueCat | Free |
| Version control | GitHub | Free |
| Design | Figma | Free |

## Monetization
- **Free:** 1 endpoint, forwarding on, 7-day history, 100 payloads/day, push notifications
- **Pro ($4.99/mo):** Unlimited endpoints, 90-day history, unlimited payloads, export, replay

## Build Order
1. ✅ Backend (Next.js API routes — create endpoint, receive webhook, forward, store)
2. ✅ Deployed to Vercel — hooksnap.vercel.app
3. ✅ Web UI — home page, endpoint dashboard, JSON viewer, diff mode (live, tested 2026-04-02)
4. ✅ Web UI quick wins — localStorage persistence, replay, copy-as-cURL, clear/delete (2026-04-03)
5. ✅ Expo mobile app (Android-first) — live and tested on device 2026-04-03
   - Home screen: create endpoint, saved endpoints (AsyncStorage), open by slug
   - Endpoint screen: payload list (polls every 5s), diff mode, clear/delete
   - Payload detail: body/headers tabs, copy-as-cURL, replay
   - Diff screen: side-by-side line diff, red/green highlights
   - `C:/Users/aspor/Documents/hooksnap/mobile`
6. ⏳ Push notifications on payload capture
7. ⏳ RevenueCat integration + paywall

## API Routes (Backend)
- `POST /api/endpoints` — create endpoint, optionally set forwardUrl, returns slug + public URL
- `GET /api/endpoints/[slug]` — fetch endpoint config
- `POST /api/h/[slug]` — receives any webhook, logs it, forwards to forwardUrl if set
- `DELETE /api/h/[slug]` — delete endpoint + all payloads
- `GET /api/h/[slug]/payloads` — returns captured payload history (default 50, max 100)
- `DELETE /api/h/[slug]/payloads` — clear all payloads
- `POST /api/h/[slug]/replay` — re-POST a captured payload to forwardUrl

## Repo
- GitHub: https://github.com/coredcon/hooksnap
- Vercel: https://hooksnap.vercel.app

## Infrastructure
- Upstash Redis: https://next-garfish-90950.upstash.io
- Payloads stored as Redis list (`payloads:[slug]`), capped at 500, 90-day TTL
- Endpoint config stored as Redis key (`endpoint:[slug]`), 90-day TTL

## Competitive Advantage Summary
| Feature | HookSnap | Webhook.site | Hookdeck | Beeceptor |
|---|---|---|---|---|
| Payload diff | ✅ | ❌ | ❌ | ❌ |
| Mobile app | ✅ | ❌ | ❌ | ❌ |
| Push notifications | ✅ | ⚠️ paid/buried | ❌ | ❌ |
| Free forwarding | ✅ | ❌ paid | ❌ | ✅ |
| Replay | ✅ | ✅ paid | ✅ | ❌ |

**Pitch:** Diff + mobile + push = unclaimed territory in this market.

## Session Notes
- 2026-04-02: Concept developed, backend built + deployed. Discussed forwarding proxy model as key differentiator over temp-URL approach. Mobile push notifications identified as the reason mobile makes sense. Competitive research confirmed no mobile app exists in this space and payload diff is unique to HookSnap.
- 2026-04-03: Web quick wins shipped (localStorage, replay, copy-as-cURL, clear/delete). Expo mobile app scaffolded and tested live on Android device — all screens working (home, endpoint list, payload detail, diff). Next: push notifications + RevenueCat paywall.
