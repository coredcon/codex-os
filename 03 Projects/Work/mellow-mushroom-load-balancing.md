# Mellow Mushroom — Load Balancing Investigation

> Living note — update as new tickets come in. Do NOT let this fall to just a digest line.

## Background / Setup

- **Chain:** Mellow Mushroom (multiple locations — same dataset pattern across all)
- **Configuration:**
  - Multiple Activity Levels
  - **AL 7:** No load balancing — items **mirror** to both Pizza Make 1 and Pizza Make 2
  - **AL 5:** Load balancing enabled — item count mode, whole orders route together to one DG
  - **AL 6:** Unknown (appears after AL5 in evening)
- **Load balancing type:** Item Count (not order count)
- **Key rule:** Items from the same order always go to the same Display Group
- **Pizza Make 1:** Display Group 1, View ID **9871**, Station(s) DG1
- **Pizza Make 2:** Display Group 2, View ID **9872**, Station(s) DG2
- **Routing:** View 9871 always routes to DG1; View 9872 always routes to DG2. LB decides which view/DG the whole order gets assigned to.

## Symptom (Customer Report)

When switching from AL 7 → AL 5, items appear to stop routing to **Display Group 1 (Pizza Make 1)**. DG2 receives all or most of the traffic.

## Historical Root Cause (from prior cases)

When the transition happens, **DG1 already has items on it from mirroring in AL 7.** The LB engine sees DG1's item count as higher than DG2's and routes new orders to DG2 until DG1 drains. This can cause an extended apparent starvation of DG1 at the start of AL5 service.

## Analysis Methodology (KitchenEvents CSV)

Columns of interest:
- `ActivityLevelID` — filter for AL 5 vs AL 7
- `Event` — `ItemCook` with a `RoutingType` = initial routing decision
- `DestinationDisplayGroup` — DG1 or DG2
- `ItemViewID` — 9871 = Pizza Make 1, 9872 = Pizza Make 2
- `ItemDGForecastPrep` — **CookTime in ms** (600 = 600ms), NOT an item count metric
- `RoutingType` — `ByCategory` = top-level item decision; `ByParentRouting` = child item following parent

**To find AL transitions:** scan for `ActivityLevelID` changes in sequence.

**To check LB balance:** count `ItemCook` events by DG/ViewID in 5-minute windows.

**To find starvation:** flag windows where DG1 count = 0 and DG2 count > threshold.

## Ticket History

### Ticket #450155 — Mellow Mushroom Hickory
- **Date:** 2026-04-06
- **Status:** Investigated
- **Finding:** KDS investigation, load balancing issue reported at AL5 transition
- **Resolution:** TBD — details not fully captured from original session

### Ticket #453260 — Mellow Mushroom [new location]
- **Date:** 2026-04-14
- **Log:** `KitchenLog-v2_20260412_050009_KitchenEvents.csv` (April 11 data)
- **AL transitions in log:**
  - 11:01 → AL 7 (start of day)
  - 16:13 → AL 0 (transition)
  - 16:14 → AL 5 (dinner service)
  - 19:53 → AL 0
  - 19:54 → AL 6
- **Finding:** LB IS working in this log — 503 items to DG1 vs 566 to DG2 over full AL5 period. No starvation at AL5 transition (DG1 gets 26 items in first 10 minutes vs DG2's 15). One 10-minute starvation window at 18:35–18:40 (LB oscillation, not transition issue). DG1 bounces back to 36 items at 18:45.
- **Open question:** Does this log show the problem, or is it a baseline? If complaint is specifically at AL7→AL5 transition, this log doesn't support that — DG1 is preferred right at transition.
- **Resolution:** LB working as expected. Customer confused by order-grouping behavior — items from same order all route to same DG, so visible counts appear unequal even when LB is correct.
- **Response sent:** Explained order-grouping logic with A/B/C/D example. Offered call to discuss further. At AL5 transition, DG1 was preferred (26 items vs DG2's 15 in first 10 min). Only starvation: 18:35–18:40 (10 min) = LB draining DG1 backlog mid-service, followed by 36-item burst at 18:45. Full shift: 503 DG1 vs 566 DG2 (52/48%). No config change needed.
- **Status:** Resolved — working as designed

## Things to Check at New Locations

1. **Item Count vs Order Count mode** — item count inflates faster due to modifiers/children
2. **Display Group Capacity setting** — if DG1 has a tighter cap than DG2, it hits ceiling faster
3. **Items on board at AL7→AL5 transition** — mirrored items still "active" on DG1 when LB evaluates
4. **CookTime difference** — if DG1 is consistently slower, item count will drift higher
5. **AL7 mirror behavior** — in AL7, both DGs show the same items; do bumps on one side clear the other?

## ⚡ First Check — Before Deep Analysis

**Both #450155 (Hickory) and #453260 resolved as "working as designed."** When a Mellow Mushroom reports DG1 starvation:
0. **Ask if they understand order-grouping** — items from the same order always route to the same DG. A 3-item order to DG2 + 1-item order to DG1 looks like "DG2 is getting everything" but is correct LB behavior. This alone resolves most complaints.
1. Pull the KitchenEvents log and check DG1 vs DG2 item counts at the AL7→AL5 transition
2. If DG1 already has items from mirroring, LB will route to DG2 until it drains — this self-corrects within minutes
3. Check overall shift balance — if 45–55% split, it's working
4. If the customer reported it and the log shows normal balance, the issue self-resolved before the log was captured
5. Ticket response: expected behavior, items resume once counts equalize

---

## LB Oscillation Pattern (observed)

When DG1 falls behind due to a large order, LB routes 100% to DG2 until DG1 drains. Once drained, LB floods DG1 with the backlog. This creates visible "dead periods" followed by bursts. Not a bug — expected behavior — but may feel broken to kitchen staff.

**Potential fix:** Adjust Display Group Capacity to allow more headroom before LB cuts off a DG.

## Related KB Articles

- `06 Resources/Freshdesk-Solutions/support/csk/-csk-how-to-set-load-balancing-to-alternate-between-two-stations.md`
- `06 Resources/Freshdesk-Solutions/internal-only/resolved-escalations/answered-question-red-lobster-what-is-the-display-group-load-balancing-logic-in-.md`
