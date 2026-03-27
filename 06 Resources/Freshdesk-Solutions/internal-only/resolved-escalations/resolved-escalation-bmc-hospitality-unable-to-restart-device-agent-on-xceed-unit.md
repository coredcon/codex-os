---
title: "*|Resolved Escalation| - BMC Hospitality - Unable to restart Device Agent on Xceed Units - Priority: High"
freshdesk_id: 17000070018
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-04-11
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000070018
---

# *|Resolved Escalation| - BMC Hospitality - Unable to restart Device Agent on Xceed Units - Priority: High

New build  Controlpoint 3.3 released 02/02/18 to resolve this issue.


Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/tickets/124899]


> 
 
**Severity:** High**Customer:** BMC Hospitality**Company ID:** Patti’s**Location / SiteID:** Patti’s**Location Found:**_"Production"_**Product:** Xceed CE**Component:** Device Agent**Version:** 3.3.105**Support Ticket #:** 124893**Date Reported:** 01/03/18**Account Manager:** Ty Reed
 
 **ISSUE**:   Unable to restart Device Agent on Xceed Units.
 When killing Device Agent from System Tray we are unable to launch DeviceAgent.exe from the Hard Disk folder therefor preventing the device from reconnecting to ControlPoint. We are using ControlPoint version 3.3.105 and CE image 2.5.3.
 **STEPS TO REPRODUCE: ** 
 1.       Remote into an Xceed unit with Server using ControlPoint Version 3.3.1052.       Close Device Agent from the System Tray3.       Try to launch Device Agent from the Hard Disk Folder.
 **ATTACHMENTS: **
 ·         Attached is the NK_2_5_3cp.bin file that will be used to update a CE image via ControlPoint.
 **IMPACT:** Requires reboot in order to get Device Agent back up and running slowing down the troubleshooting of CE devices.
 **WORKAROUND:**  Have the client reboot the device or run “Upgrade Device Agent” to force a restart remotely.