---
title: "*|Resolved Escalation| - DARDEN / LONGHORN - Items fail to display on Grill Station - Priority: High"
freshdesk_id: 17000069619
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-04-02
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069619
---

# *|Resolved Escalation| - DARDEN / LONGHORN - Items fail to display on Grill Station - Priority: High

(03/28) - JSE - New build  7.3 Release 1 certified on 03/27 to resolve this issue.


 Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/tickets/129018]


>  
**Severity:**High**Customer:**Darden – Longhorn**Company ID:**N/A**Location / SiteID:**N/A**Location Found:**_"Production"_**Product:**Kitchen Server **Component:**Kitchen Server**Version:**7.2.108.0**Smoke Test (Y \ N)**N**Support Ticket #:**128456**Date Reported:**02/24/2018**Account Manager:**Nina Kovach  **ISSUE**:   Items fail to display on Grill Station but scroll queue counters continue to increment.  NOTE:   This has been recreated and already reported to Dev.   Issues with the FD – Jira integration prevented entering ticket prior to today.   **Jira Ticket # KS-1191** has been created to track the fix.   Around 18:38 or so they noticed they were missing several orders on Grill (station 11) that they could see on the QB screen. There were only 4 orders on the Grill screen but the counter on the right of screen indicated 11 orders off screen.  Restarting the station resolved the display issue. **STEPS TO REPRODUCE: ** (_include screenshots if available_) 

- Start Kitchen Server with Site Dataset.

- Enter items from POS to fill the line item on station 2 so that there is 1 item in the right scroll queue.

- Select the bottom item that is partially displayed.

- Press the “End” Base action key.

- Enter more items from the POS.   They do Not display on the available space on the Grill screen, though as more items added the right scroll counter increases
 **ATTACHMENTS:  **(_describe attachments below_) 

-  Log files/Capture images are included in the following link: 
 **IMPACT:**  Requires addition of redraw key to ensure the display is up to date **WORKAROUND:**  Suggested adding a combo action of end/redraw until a fix could be provided.