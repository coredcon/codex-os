---
title: "Unable to Create Template in ControlPoint due to: Error sending revision 'Default' to server"
freshdesk_id: 17000147074
category: "Support"
folder: "In Progress"
status: published
created: 2025-07-01
updated: 2025-07-16
views: 0
tags: ["ControlPoint", "Revision"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000147074
---

# Unable to Create Template in ControlPoint due to: Error sending revision 'Default' to server

**Problem:  **Caller reports receiving an error when attempting to create a template within ControlPoint.


 


**Reason behind error being displayed:**


The ControlPoint is trying to write to the following file path: C:\ProgramData\QSR Automations\ConnnectSmart\ControlPointClient\Cache, but the account being used does not have the proper permissions to read & write to the folder within the C:\ProgramData\QSR Automations\ file path.


**Troubleshooting Steps:**


1. Confirm that the account that is signed in to the Server has Read and Write permissions for all QSR folders within the C:\ProgramData\QSRAutomations folder and all folders within it. 


2. This is preferred to be done by the tech that has called in to report the issue, due to possible limitations of editing the folder permissions yourself.

2. Once that has been completed, you should now be able to create a template within ControlPoint without receiving tan error message.


Related Ticket: [https://qsrautomations.freshdesk.com/a/tickets/402333]