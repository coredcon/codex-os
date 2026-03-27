---
title: "*|Resolved Escalation| - THE MELT - Web Events backup error - Priority: Medium"
freshdesk_id: 17000069639
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-04-03
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069639
---

# *|Resolved Escalation| - THE MELT - Web Events backup error - Priority: Medium

The Bug Was Fixed As Part Of Ks-149 Allow Both Primary And Secondary Kitchenserver Instances To Register With Enterprise Which Was In Kitchen Server 7.0 R1


Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/tickets/128191]


> 

 
**Severity:**Medium**Customer:**THE MELT (LAB 2)**Company ID:**9122667**Location / SiteID:**137430/150324**Location Found:**_Customer Lab_**Product:**CSK 6.4.111**Component:**Web Events Service 6.0**Version:**6.4.109**Smoke Test (Y \ N)**N**Support Ticket #:**127520**Date Reported:**02/12/2018**Account Manager:**Michael Prager
 
 **ISSUE**:   Web Events error on backup device
 Backup server returns an error message when attempting to subscribe to Web Events…WebServiceRequestValidator.cpp,83,CEventsRequestValidator::ValidateRequest,QSR-Authorization key does not allow Events without license feature
 **STEPS TO REPRODUCE:**
 1.       Connected to site and recorded session of Chris from The Melt stopping and restarting services on primary and backup device, multiple times, with the same error message
 ·         **ATTACHMENTS:  **[https://qsrautomations.sharefile.com/d-sb2ba7adeefb4c8da]
 Data set, Kitchen Server log file from primary and backup, recorded remote session showing steps site takes to reproduce the error. Screen shot of Bin Files from primary and backup device
 
 **IMPACT:** Medium, site cannot function fully when in backup mode
 **WORKAROUND:**  None