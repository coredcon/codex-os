---
title: "*|Resolved Escalation| - DARDEN - Cursor disappears from item screen during a controller reboot if cursor was on an item that gets rerouted - Priority: Normal"
freshdesk_id: 17000077836
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-09-06
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000077836
---

# *|Resolved Escalation| - DARDEN - Cursor disappears from item screen during a controller reboot if cursor was on an item that gets rerouted - Priority: Normal

(09/06) - CC - CSK 8.0.1 released 04/28/18 addressed this issue


Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/tickets/131059]


> On Mon, 2 Apr at 9:32 AM , QSR Support Team <supportteamdistro@qsrautomations.com> wrote:Team, Please see the escalation, below. 
**Severity:** Normal**Customer:** Darden**Company ID:** Darden**Location / SiteID:** All**Location Found:**Production**Product:** ConnectSmart Kitchen**Component:** Kitchen Server**Version:** 7.3**Smoke Test (Y \ N)**N**Support Ticket #:** 131002**Date Reported:** 03/30/2018**Account Manager:** Nina Kovach  **ISSUE**:   Customer advises that if a controller gets rebooted while items are on the screen, and the items are rerouted when the cursor is on any item but the top item, then the cursor is unavailable when the next item is rang in It appears that when a station is restarted, Kitchen remembers the cursor’s last location so that when it comes back up, the same item is marked by the cursor. In the case when the items are rerouted, that location is no longer valid. This gets reset when a second new item is rang in, presumably causing the system to recalculate item display positions.  **STEPS TO REPRODUCE: **  1)      Place 4 orders from POS that route to the Fish Grill station and send to kitchen 2)From the Fish Grill view, move cursor to the 3rd item 3)Power off controller 4) Wait 60 seconds for the items to re-route to Meat Grill station 5)Power on Fish Grill controller 6)Place a new order that routes to Fish Grill station 7)Item appears, but cursor does not 8)Select Cook button, and get msg "Cook invalid, no item to cook" 9)Ring in another item to appear on Fish Grill, and cursor appears              **ATTACHMENTS:  ** ·         Dataset for Seasons 52·         KitchenLog Darden DB·         KitchenServer Darden Log·         KitchenServer Darden Capture.QSRCap **IMPACT:**   **WORKAROUND:**  In the Item View Template >>  General >> Check the option "When scrolled, automatically home after (set to 60) seconds of inactivity". This means that if the station is offline long enough to reroute items, In this instance 60 seconds, then the system will reset the cursor back to the first location.