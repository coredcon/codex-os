---
title: HookSnap
status: In Progress
started: 2026-04-02
last_updated: 2026-04-04
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

### Payment Strategy
- **Web-only checkout via Stripe** — no in-app payment UI on mobile (avoids 30% Google Play cut + policy risk)
- Mobile app never solicits payment. Pro-gated feature limits just say "visit hooksnap.app to upgrade"
- On purchase: Stripe webhook → backend stores Pro token in Redis → email token to user
- User pastes Pro token into mobile app once (Settings screen) — stored in AsyncStorage
- No passwords, no OAuth, no sessions. Email is the only identity.
- RevenueCat / Play Store billing deferred — revisit if mobile-native purchases become a priority

### Plans
| | Free | Pro |
|---|---|---|
| Endpoints | 1 | Unlimited |
| History | 7 days | 90 days |
| Payloads/day | 100 | Unlimited |
| Forwarding | ✅ | ✅ |
| Push notifications | ✅ | ✅ |
| Replay | ✅ | ✅ |
| Export | ❌ | ✅ |
| **Monthly** | $0 | **$9/mo** |
| **Annual** | $0 | **$79/yr (~$6.58/mo)** |

### Pricing rationale
- $9/mo matches Webhook.site, well under Hookdeck ($25+)
- Target users (TAMs, integration engineers) expense dev tools without approval
- $4.99 reads as hobby project — $9 signals a real product
- Annual plan locks in retention + provides upfront cash

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
6. ✅ Push notifications on payload capture (2026-04-03) — FCM V1 via Expo, Firebase configured, working on device
7. ✅ App icon designed + deployed (2026-04-03) — emerald hook-arrow, dark bg, matches brand
8. ✅ Landing page hero (2026-04-03) — pitch + feature pills + creator below
9. ✅ Icon in web header + endpoint page nav (2026-04-03)
10. ✅ Notification tap navigation (2026-04-03) — tapping push goes to endpoint screen
11. ✅ Forward URL edit on web + mobile (2026-04-03)
12. ✅ Content-type badge + forward status indicator on payload rows (2026-04-03)
13. ✅ Stripe integration (web checkout → Pro token → Redis → email delivery) — fully built 2026-04-04
    - `/api/stripe/checkout` — creates Stripe Checkout session (monthly/annual)
    - `/api/stripe/webhook` — `checkout.session.completed` → nanoid Pro token → Redis → Resend email; `customer.subscription.deleted` → token revoke
    - `/api/stripe/recover` — resend token by email lookup
    - `/api/pro/verify` — validate Pro token, return plan info
    - `/upgrade` page — pricing cards (Free vs Pro), monthly/annual CTA
    - `/settings` page — Pro token entry + verify flow
    - `stripe` + `resend` packages installed
14. ✅ Deploy Stripe to Vercel prod — Stripe working end-to-end, token email confirmed received
15. ✅ Pro feature gating (2026-04-04)
    - Endpoint creation: 1 endpoint cap for free (by IP)
    - Payload history: 7-day filter for free, 90-day for Pro
    - Payloads/day: 100/day cap for free on webhook receiver (keyed `payload_count:{slug}:{date}`, 25h TTL)
    - **Admin bypass:** `ADMIN_PRO_TOKEN` env var — skips all plan checks
16. ✅ Settings screen on mobile (2026-04-04)
    - Plan badge (Free/Pro), feature list, Upgrade CTA → hooksnap.app/upgrade
    - Pro token entry with verify → `GET /api/pro/verify`, persisted in AsyncStorage
    - Token masked display + remove token option
    - Recover link → hooksnap.app/upgrade/recover
    - Gear icon in home header → `/settings`
16. ✅ Privacy Policy + Terms of Service — web pages + mobile links (2026-04-04)
    - `/privacy` and `/terms` pages on web with footer links on upgrade/privacy/terms pages
    - Privacy/Terms links in mobile Settings screen → open in browser
    - `PlanBadge` component in upgrade + settings headers; Pro pill or "Free · Upgrade" link
    - Double billing blocked — upgrade page checks localStorage token; if Pro, shows status view, no checkout buttons
17. ✅ Endpoint naming (2026-04-04)
    - Optional name field on endpoint creation (web + mobile)
    - Inline name edit on web endpoint detail page (click to edit, PATCH to API)
    - Name bar on mobile endpoint screen (same tap-to-edit UX)
    - Name displayed in saved endpoint list on web home + mobile home
    - Bug fixed: `POST /api/endpoints` response was missing `name` field — names set at creation weren't saved to localStorage
    - localStorage purge: `loadSaved()` now filters `!!e.slug` and removes invalid entries (clears blank endpoints from previous bug)
    - Home page freshness fix: `visibilitychange` listener re-reads localStorage on back-navigation (Next.js App Router caches pages)
18. ✅ Domain migration → hooksnap.app (2026-04-04)
    - Purchased `hooksnap.app` on Porkbun
    - Added to Vercel Domains — A record `@` → `216.198.79.1`, CNAME `www` → Vercel DNS
    - Fixed conflicting CNAME on Porkbun root (`@`) — deleted stale CNAME before A record could be added
    - Updated all API routes: `process.env.BASE_URL || process.env.NEXT_PUBLIC_BASE_URL || 'https://hooksnap.app'`
    - Added `BASE_URL=https://hooksnap.app` as server-side Vercel env var (more reliable than `NEXT_PUBLIC_*` in API routes)
    - Updated Stripe success/cancel/return URLs in Vercel env vars
    - Updated mobile `BASE_URL` in `lib/api.ts` from `hooksnap.vercel.app` → `hooksnap.app`
    - Updated all hardcoded URLs in mobile payload detail screen
    - Fixed portal 500 — trailing newline in `NEXT_PUBLIC_BASE_URL` from `echo` pipe → "Not a valid URL". Fixed by re-adding env var cleanly + `.trim()` in code.
19. ✅ Stripe Customer Portal — plan switching (2026-04-04)
    - `/api/stripe/portal` route: looks up Stripe customerId from Redis, creates billing portal session
    - "Switch to Annual · save 27% →" button in Settings if plan is monthly — POSTs to portal route, redirects to Stripe
    - Portal returns user to `/settings` after changes
    - Stripe dashboard: enabled "Customers can switch plans" with proration (charges annual minus credit for remaining monthly time — no overlap)
    - Portal wrapped in try/catch — surfaces real Stripe errors in browser alert instead of silent 500
    - Added `interval` field to `getPlan()` return and `GET /api/pro/verify` response
20. ⏳ EAS production build + Play Store submission
21. ⏳ Switch Stripe to live/production keys
22. ⏳ Dashboard — all-endpoints status + stats view (all users)

## Tech Stack Reference

### Backend
| Tool | Role |
|---|---|
| **Next.js** | Web framework — serves API routes + web UI. Each API route = a serverless function on Vercel. |
| **TypeScript** | Typed JavaScript — catches bugs before they ship. |
| **Vercel** | Hosting. Serverless — spins up on demand, free until real traffic. |
| **Upstash Redis** | Database. Stores endpoint configs + captured payloads as key-value data. HTTP-accessible so it works inside Vercel serverless functions. Free tier is generous. |
| **@upstash/ratelimit** | Rate limiting layer on the webhook receiver. Counts requests per slug/min, blocks abuse. |

### Mobile
| Tool | Role |
|---|---|
| **Expo** | Toolchain for React Native — avoids raw Android Studio/Xcode. Handles OTA JS updates. |
| **React Native** | One JS codebase → native Android (and eventually iOS) app. |
| **AsyncStorage** | On-device local storage. Holds ownerTokens, saved endpoint slugs, push token. |
| **Expo Notifications** | SDK for requesting push permission + getting Expo push token. |
| **Firebase / FCM** | Google's push delivery service. Expo uses it under the hood for Android. Configured via `google-services.json`. |
| **EAS** | Builds the actual APK/AAB for Play Store. The compile-and-package step. |

### Payments (planned)
| Tool | Role |
|---|---|
| **Stripe** | Web checkout, card processing, fires webhook to backend on payment. Never touches card data directly. |

### Data Flow
- **Webhook received:** Source POSTs → Vercel function → stored in Upstash → Expo push fires via Firebase → phone buzzes
- **User pays:** Stripe Checkout → Stripe webhook → backend stores Pro token in Upstash → emails token → user pastes into app

## Cross-Device / Free Tier Model
- Free tier is **device-local** — the ownerToken lives where the endpoint was created
- Typical flow: create endpoint on web → copy slug → open in mobile app → push notifications register via ownerToken
- "Open by Slug" on mobile gives view-only if ownerToken isn't present; prompt to enter token for full access
- Cross-device sync (ownerToken accessible on multiple devices) = **Pro feature**
- Push notifications work on free tier — mobile is the point, not a gated feature

## API Routes (Backend)
- `POST /api/endpoints` — create endpoint, optionally set forwardUrl + name, returns slug + public URL + ownerToken
- `GET /api/endpoints/[slug]` — fetch endpoint config
- `PATCH /api/endpoints/[slug]` — update name and/or forwardUrl (requires ownerToken)
- `POST /api/h/[slug]` — receives any webhook, logs it, forwards to forwardUrl if set
- `DELETE /api/h/[slug]` — delete endpoint + all payloads
- `GET /api/h/[slug]/payloads` — returns captured payload history (default 50, max 100)
- `DELETE /api/h/[slug]/payloads` — clear all payloads
- `POST /api/h/[slug]/replay` — re-POST a captured payload to forwardUrl
- `POST /api/stripe/checkout` — create Stripe Checkout session (monthly/annual)
- `POST /api/stripe/webhook` — handle Stripe events (provision/revoke Pro)
- `POST /api/stripe/portal` — create Stripe billing portal session (plan switching)
- `POST /api/stripe/recover` — resend Pro token to email
- `GET /api/pro/verify` — validate Pro token, returns plan + email + interval

## Stripe / Resend Config
> Test mode keys — swap for live keys when ready to charge real money

| Var | Value |
|---|---|
| `STRIPE_PRICE_ID_MONTHLY` | `price_1TILZIPWsQgeW7zULQxnfzTJ` |
| `STRIPE_PRICE_ID_ANNUAL` | `price_1TILaePWsQgeW7zU15OwkTUv` |
| `RESEND_FROM_EMAIL` (test) | `HookSnap <onboarding@resend.dev>` |
| `RESEND_FROM_EMAIL` (live) | `HookSnap <noreply@hooksnap.app>` |

> Secret keys (STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET, RESEND_API_KEY) live in Vercel env vars only — not stored here.

## Repo
- GitHub: https://github.com/coredcon/hooksnap
- Live: https://hooksnap.app (domain migrated 2026-04-04)
- Vercel project: `hooksnap` (NOT `backend` — stale project, ignore it)

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

## Security Status
> Last reviewed: 2026-04-03

| # | Issue | Severity | Status |
|---|---|---|---|
| 1 | SSRF via forwardUrl (no URL validation — can target AWS metadata, internal IPs) | Critical | ✅ Fixed |
| 2 | Push token poisoning (anyone can subscribe to any slug's notifications) | Critical | ✅ Fixed |
| 3 | No rate limiting on webhook receiver (abuse/cost risk) | High | ✅ Fixed |
| 4 | Unbounded payload size (`request.text()` with no cap) | High | ✅ Fixed |
| 5 | Ownership token model (slug is only key — no auth for writes/deletes) | High | ✅ Fixed |
| 6 | Error detail leakage in replay route (`detail: String(err)`) | Medium | ✅ Fixed |
| 7 | Sensitive headers stored verbatim (auth tokens visible to anyone with slug) | Medium | By design — warn users |

### Notes
- SSRF: Block private IP ranges (10.x, 192.168.x, 127.x, 169.254.x) and non-http/https at forwardUrl write time
- Ownership: Before Pro tier, return a `ownerToken` at endpoint creation; require it for PATCH/DELETE/replay
- Rate limiting: Upstash has a built-in rate limit SDK — apply to `POST /api/h/[slug]`
- Push token poisoning: Tie token registration to ownership token once that system exists

## Session Notes
- 2026-04-02: Concept developed, backend built + deployed. Discussed forwarding proxy model as key differentiator over temp-URL approach. Mobile push notifications identified as the reason mobile makes sense. Competitive research confirmed no mobile app exists in this space and payload diff is unique to HookSnap.
- 2026-04-03: Web quick wins shipped (localStorage, replay, copy-as-cURL, clear/delete). Expo mobile app scaffolded and tested live on Android device — all screens working (home, endpoint list, payload detail, diff). Next: push notifications + RevenueCat paywall.
- 2026-04-03 (continued): Push notifications fully working on device. Required: Firebase project + google-services.json in build, FCM V1 service account uploaded to Expo via `eas credentials`. EAS dev build rebuilt with Firebase. Next: RevenueCat paywall.
- 2026-04-03 (security + monetization): Full security audit completed — SSRF, rate limiting, ownership tokens, payload size cap, push token poisoning all fixed and deployed. RevenueCat dropped in favor of Stripe web-only checkout. Pricing set at $9/mo / $79/yr. Free tier is device-local; cross-device sync is a Pro feature. Push notifications available on free tier. No full user accounts — email + Pro token is the identity model.
- 2026-04-04 (domain + gating + naming + portal): Domain migrated to hooksnap.app. Full Pro feature gating live (endpoint cap, history filter, payloads/day). Mobile Settings screen built. Privacy/Terms pages + PlanBadge component. Double billing protection on upgrade page. Endpoint naming (optional, on creation + inline edit). Stripe Customer Portal wired for plan switching (monthly → annual with proration). Major bugs fixed: Vercel wrong project, undefined slug saved to localStorage, name missing from create response, portal 500 from trailing newline in env var, App Router cache staleness on home page. All mobile URLs updated to hooksnap.app. Next: EAS production build, Stripe live keys, dashboard.
