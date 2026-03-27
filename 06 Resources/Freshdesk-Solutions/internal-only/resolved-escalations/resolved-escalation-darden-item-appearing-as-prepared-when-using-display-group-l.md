---
title: "*|Resolved Escalation| - DARDEN - Item appearing as prepared when using display group load balancing, preventing accurate demand projections - Priority: Medium"
freshdesk_id: 17000077839
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-09-06
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000077839
---

# *|Resolved Escalation| - DARDEN - Item appearing as prepared when using display group load balancing, preventing accurate demand projections - Priority: Medium

(09/06) - CC - CSK 8.0 released 06/26/18 addressed this issue


Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/tickets/132474]
> On Mon, 16 Apr at 4:11 PM , QSR Support Team <supportteamdistro@qsrautomations.com> wrote:Team, Please see the escalation, below. 
**Severity:** Normal**Customer:** Darden**Company ID:** YardHouse**Location / SiteID:** All**Location Found:**_Production_**Product:** ConnectSmart Kitchen**Component:** Kitchen Server**Version:** 7.3**Smoke Test (Y \ N)**N**Support Ticket #:** 132409**Date Reported:** 04/04/2018**Account Manager:** Nina Kovach  **ISSUE**:   Item appearing as prepared when using display group load balancing, preventing accurate demand projections When the Fruit item hits the Pantry2 due to load balancing, it is being marked as Prepared on the Expo, preventing the Fruit counter from incrementing properly. **STEPS TO REPRODUCE: **  1.       Open only Expo 1 (11), Pantry 1 (17), and Pantry 2 (18) clients so other items will go prepared automatically (this isn’t necessary, just speeds up testing process).2.       Run the attached Capture file. Order appears on Expo, Fruit appears on Pantry 1. Fruit Counter Increments by 1.  3.       Run Capture again. Order appears on Expo, Fruit appears on Pantry 2. Fruit shows as prepared on Expo, Fruit counter does not increment.   4.       Run Capture additional times. Each time the Fruit appears on Pantry1, it is unprepared, Fruit counter goes up. Each time it hits Pantry 2, it is prepared and counter does not increment.5.       Marking the Fruit as Cooking on Pantry 2 makes the item now show as Unprepared on Expo, but Counter still does not Increment.  **ATTACHMENTS:  ** ·         Dataset: YHK1_CS_0.1.6_132409·         Capture: Fruit_as_appetizer_132409.qsrcap·         Transaction DB: Darden DB_132409.xls **IMPACT:**  Can cause site to lose an item thinking it has already been prepared, resulting in customer’s missing food items. **WORKAROUND:**  Site currently has a workaround in place not using Load Balancing.