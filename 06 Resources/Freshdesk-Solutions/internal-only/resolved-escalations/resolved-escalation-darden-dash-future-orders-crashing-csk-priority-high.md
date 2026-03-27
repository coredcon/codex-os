---
title: "*|Resolved Escalation| - DARDEN - Dash future orders crashing CSK - Priority: High"
freshdesk_id: 17000069631
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-04-03
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069631
---

# *|Resolved Escalation| - DARDEN - Dash future orders crashing CSK - Priority: High

(04/04) - CC -  New Build release on 03/27/18 to resolve this issue


Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/tickets/128570]


> 

 
**Severity:**High**Customer:**Darden**Company ID:**Darden**Location / SiteID:**Darden**Location Found:**_Lab_**Product:**CSK**Component:**KitchenServer**Version:**7.3.102**Smoke Test (Y \ N)**N**Support Ticket #:**None **Date Reported:**02/26/2018 **Account Manager:**BWayne
 
 **ISSUE**:   Dash future orders crashing CSK
 For the attached Dash order (Dash-Order.txt, customer name crash21) I checked the box for “Allow future order delay” in the dataset and set the Quoting Scheme “Package Time” to 1 second for Item and Course package time. I placed the order in Dash with a future time, then released it immediately. CSK held it the proper amount of time and displayed it when it should have. This order worked perfect. **STEPS TO REPRODUCE:**
 For the attached Dash order (Dash-Crash.txt, customer name crash22) I unchecked the box for “Allow future order delay”.I placed the order in Dash with a future time, then released it immediately.This order crashed CSK as soon as it was released. The only difference was checking box for “Allow future order delay”.
 **ATTACHMENTS:**
 The crash dump for the crashed order is located here The dataset is attached.