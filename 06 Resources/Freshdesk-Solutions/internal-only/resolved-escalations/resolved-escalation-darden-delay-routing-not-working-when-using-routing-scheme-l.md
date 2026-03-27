---
title: "*|Resolved Escalation| - DARDEN - Delay Routing Not Working When Using Routing Scheme Load Balancing - Priority: High"
freshdesk_id: 17000071059
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-05-01
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000071059
---

# *|Resolved Escalation| - DARDEN - Delay Routing Not Working When Using Routing Scheme Load Balancing - Priority: High

(05/01) - JSE - CSK Server 7.3 P1


KS-1171 "FIx Delay Routing Not Working When Using Routing Scheme Load Balancing" Released: 5/1/18


Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/tickets/124874]


> On Wed, 3 Jan at 2:04 PM , QSR Support Team <supportteamdistro@qsrautomations.com> wrote:Team,
 Please see the escalation, below.
 
**Severity:** High**Customer:** Darden**Company ID:** Olive Garden**Location / SiteID:** Olive Garden**Location Found:**_"Customer Lab" or "Production"_**Product:** CSK Kitchen Server**Component:** Delay Routing/Load Balancing**Version:** 7.2.106**Support Ticket #:** 124871**Date Reported:** 01/03/18**Account Manager:** Nina Kovach
 
 **ISSUE**:   Delay Routing not working when using Routing Scheme load balancing.
 When Routing Scheme Load balancing is enabled on the “Saute Load Balance” routing scheme, the Saute item immediately displays on either Saute 1 or Saute 2 when the order is sent in.
 **STEPS TO REPRODUCE: ** 
 1.       Play the attached capture.  It sends two items – one that routes to Grill with 600 second cook time, and another that routes to Saute with a 570 second cook time.  When Routing Scheme Load balancing is enabled on the “Saute Load Balance” routing scheme, the Saute item immediately displays on either Saute 1 or Saute 2 when the order is sent in.2.       If you disable the load balancing on the Saute Load Balance routing scheme, the item properly displays on Saute 30 seconds after the Grill item is cooked, but it displays on both Saute screens, instead of load balancing between the two.
 **ATTACHMENTS: **
 ·         !OG 20180101AM-GXR.zip – Dataset used for testing·         OliveGarden Load Balancing Bug.qsrcap – Capture file used for testing.
 **IMPACT:**  High as it removes a functionality of Kitchen that is regularly used.
 **WORKAROUND:**  None at this time discovered.