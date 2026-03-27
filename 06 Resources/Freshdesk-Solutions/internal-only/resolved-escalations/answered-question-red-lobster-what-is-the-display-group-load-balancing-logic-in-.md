---
title: "*|Answered Question| - RED LOBSTER - What is The Display Group Load Balancing Logic in Determining Item Count - Priority: Normal"
freshdesk_id: 17000069642
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-04-03
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069642
---

# *|Answered Question| - RED LOBSTER - What is The Display Group Load Balancing Logic in Determining Item Count - Priority: Normal

The display group item count only includes items that are routed as top-level items on at least one view in the display group. It does not depend on the item type (food item, side item, condiment), only on whether the item is a top-level item on a view in the display group. Also, once the item has been prepared in the display group, it no longer counts towards the display group's item count.

The metrics that kitchen server uses in determining the display group item counts for load balancing can be configured on dashboard views using the Display Group Metric Field with Use Load Balancing Metrics enabled (see screenshot below). The two relevant metrics are Items Active and Items Prepared_. It may be useful for the customer to add those metrics for each display group to a dashboard in order to see the counts in specific examples. The current item count for a display group is calculated as (_Items Active – Items Prepared_). For example if there are 3 items active in the display group, but one has already been prepared (bumped off of all prep views in the display group), then the item count for the display group is 2.
 

In the example mentioned in this ticket, the counts depends on which items are routed to views in the display group, and whether those items are considered "prepared" in the display group. For example, if "CYOP 3" routes to all views along with all its children, then "CYOP 3" would be the only top-level item in the display group and the item count would be 1 (_Items Active = 1, Items Prepared = 0). When that item is bumped from all prep views, the item count would be 0 (Items Active = 1, Items Prepared = 1). However, if the "Catfish", "Shrimp", and "Lobster" child items routed independently from their parent and display as 3 separate top-level items on some view in the display group, then each of those would also count towards the item count. Assuming the"CYOP 3" also routes to a view in the display group, Items Active would be 4 and Items Prepared would increment as items are bumped from prep views. Note that the point when the "CYOP 3" parent item is considered prepared in this case depends on the Derive parent item statuses from child items if the parent item does not route to prep views setting (see KS-975). If disabled, "CYOP 3" would be considered prepared immediately since it does not route to any prep views. If enabled, "CYOP 3" would be considered prepared once all its child items have been prepared.


> On Fri, 30 Mar at 4:30 PM , QSR Support Team <supportteamdistro@qsrautomations.com> wrote:Team, Please see the escalation, below. 
**Severity:** Normal**Customer:** Red Lobster**Company ID:** Red Lobster**Location / SiteID:**All Sites**Product:** ConnectSmart Kitchen Server**Component:** Display Group Load Balancing by Item Count**Version:** 7.3.102**Support Ticket #:** 129984**Customer:** Red Lobster  **QUESTION: How is the Item Count determined in Display Group Load Balancing?**Client would like to know the specifics of how Item Count is determined when using Display Group Load Balancing By Item Count. Does it count every Item Type or does it exclude certain item types like piece detail, condiment, combo item, etc. Does it only look at the parent item and counts it as one items or do the component items also factor in to the Item Count? Do items from the same transaction number but different courses route to the same Display Group? In the example below the client would like to know how many items would be counted to determine the Item Count for the Display Group? Parent: CYOP 3 – Combo Item                Child: Catfish – Food Item                Child: Shrimp – Piece Detail                Child: Lobster – Food Item **ATTACHMENTS:  **Red Lobster 129984 Load Balancing.zip·         Red Lobster 129984 Load Balancing - Dataset·         Red Lobster Shortened Capture – Capture file·         Alley 1 and Alley 2 Red Lobster – Screenshot of the Alley 1 and Alley 2 screens out of balance.·         Red Lobster DB – Excel breakdown of Red Lobster DB. The Alley 1 and Alley 2 Tab in the document has a breakdown of the item type counts and how many items each display group was routed.·         Red Lobster.db – SQL lite DB file