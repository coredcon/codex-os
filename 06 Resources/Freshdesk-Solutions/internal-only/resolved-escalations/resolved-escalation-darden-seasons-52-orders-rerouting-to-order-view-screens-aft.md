---
title: "*|Resolved Escalation| - DARDEN (Seasons 52) - Orders rerouting to Order View screens after activity level change - Priority: Medium"
freshdesk_id: 17000071062
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-05-01
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000071062
---

# *|Resolved Escalation| - DARDEN (Seasons 52) - Orders rerouting to Order View screens after activity level change - Priority: Medium

(05/01) - JSE -  CSK Server 7.3 P1


"Activity level change causes orders to reroute after they have previously been bumped" Released: 5/1/18


[]


Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/t]ickets/128752


[]


> On Wed, 28 Feb at 5:38 PM , QSR Support Team <supportteamdistro@qsrautomations.com> wrote:Team, Please see the escalation, below. 
**Severity:** Normal**Customer:** Darden**Company ID:** Seasons 52**Location / SiteID:**  Seasons 52**Location Found:**_"Customer Lab"_**Product:** ConnectSmart Kitchen Server**Component:** Reroute Transactions feature in View Manager**Version:** CSK 7.2.106**Support Ticket #:** 128747**Date Reported:** 02/28/18**Account Manager:** Nina Kovach  **ISSUE**:   Orders rerouting to Order View screens after activity level change. The site is using the “Reroute Transaction” method for changing Activity Levels and Orders will reappear on Order View Screens if all order view screens have not bumped it off. In the case provided they have an Assembler Station (Station 14) and a Expo Station (Station 18). We ring up an item with department 6 and it will appear on Station 14 and Station 18. If you bump the order off of Station 14 and change Activity Level 1 to Activity Level 3 then you will observe the order reappear on Station 14. The station type for station 14 is Assembler and Station 18 is Expediter. I have tested with all types of the Fixed Grid View (Expediter, Assembler, Prep) and the behavior noticed was across all types for Station 14. I even changed the fixed grid to a flex grid and observed the same behavior. It appears that if an Order is still active on an Expediter screen, when an activity level change occurs, that the order will reroute to each Order View that it had previously been bumped from. **STEPS TO REPRODUCE: **  1.       Run the attached capture file2.       If you want to manually test then you can ring in an item with Department 6 and then bump it off of Station 14 which is the Assembler station.3.       After that you would need to change Activity Levels from 1 to 3.4.       You will notice that the item bumped off will reappear on Station 14 after the activity level change has been completed. **ATTACHMENTS:  ** ·         Seasons 52 Activity Level Ticket 128747.db – Kitchen Log DB·         Seasons 52 Activity Level Ticket 128747.log – Kitchen Log txt·         Seasons 52 Activity Level Ticket 128747.qsrcap – Capture File·         Seasons 52 Dataset Activity Level Ticket 128747 - Dataset **IMPACT:**  Prevents customer from using their preferred method of routing when changing activity levels. **WORKAROUND:**  None currently exist