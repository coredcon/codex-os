---
title: "ControlPoint: Unauthorized Access Error"
freshdesk_id: 17000145746
category: "Support"
folder: "ControlPoint"
status: published
created: 2025-03-26
updated: 2025-04-17
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000145746
---

# ControlPoint: Unauthorized Access Error

**ControlPoint Unauthorized Access Error:**


_Error sending revision ‘Default’ to Server_


 


**Problem:** The following error appears while creating a template in ControlPoint:


 Error Details:


The details for this ControlPoint Client-specific error indicate there was an Unauthorized Access error while attempting to write to a temporary file in 


C:\ProgramData\QSR Automations\ConnectSmart\ControlPointClient\Cache 


**Resolution:** The User account being utilized and the Administrator Group need to have Read & Write access to the Cache folder, along with all folders in C:\ProgramData\QSR Automations


 


 


Once this has been completed, you can continue creating the template. 


**Ticket Reference:** https://qsrautomations.freshdesk.com/a/tickets/402333