---
title: "*|Resolved Escalation| - US BEEF - RDS Stations not showing Side Items Independently - Priority: High"
freshdesk_id: 17000069772
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-04-05
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069772
---

# *|Resolved Escalation| - US BEEF - RDS Stations not showing Side Items Independently - Priority: High

(04/05) - CC -  Issue resolved in 7.3 release 3/27/18


Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/tickets/125605]


> 

 
**Severity:**High**Customer:**ARBYS**Company ID:**ARBYS**Location / SiteID:**ARBYS**Location Found:**_Production_**Product:**ConnectSmart Kitchen Server**Component:**RDS Station Routing**Version:**7.2.108**Support Ticket #:**125599**Date Reported:**01/15/18**Account Manager:**Kevin Clements
 
 **ISSUE**:  Side Items are not properly routing to RDS Screens when sent as a child item. It is creating a blank order with a header.
 Items  are not properly routing to RDS Screens when sent as a child item. It is creating a blank order with a header. The RDS Fry Station is station 2 and the GRDS version of the Fry is Station 8. Every Fry Order properly displays on the GRDS station 8. The break appears to be correlated with the Display of Child Items when the parent item is not set to route to that station.
 **STEPS TO REPRODUCE: ** 
 1.       Run your Epic Emulator for RDS Station 2 and Display Client for GRDS station 82.       Run the attached capture file. Transaction 26 is where I sent the Curly fry as a child of Brisket. Transaction 27  is the Sm Curly order by itself in which it displays correctly. . Results and SocketMon Below:
 **ATTACHMENTS: **
 ·         US Beef – RDS.zip = Dataset·         Arbys Ticket 125599.qsrcap – Capture file for the above testing
 **IMPACT:**  High as it is preventing implementation at site due to child items not displaying on their RDS stations.
 **WORKAROUND:**  None currently discovered to associate child items with parent items.