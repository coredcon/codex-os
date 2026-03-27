---
title: "DisplayClient Crashing Due to VirtualStore QSR Directory"
freshdesk_id: 17000138369
category: "Support"
folder: "In Progress"
status: published
created: 2024-01-09
updated: 2024-01-09
views: 0
tags: ["DisplayClient", "VirtualStore", "Crashing", "Display Client"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000138369
---

# DisplayClient Crashing Due to VirtualStore QSR Directory

**Description of Problem**


In cases where permissions issue block DisplayClient from accessing the ProgramData folder, Windows may create a VirtualStore folder and store the ConnectSmartNetwork.xml and other files there. As this works as an override folder, Windows will then reference these files instead of the correct location in C:\Users\qsr\AppData\Local\VirtualStore\ProgramData\QSR Automations\ConnectSmart\QsrDisplayClient\Data. **This can cause the DisplayClient to crash repeatedly when the template is applied.**


**Short Term Fix**


- Disable the DisplayClient template in ControlPoint for the problem station.

- On the station where DisplayClient crashes look for the **C:\Users\qsr\AppData\Local\VirtualStore\ProgramData\QSR Automations\ConnectSmart\QsrDisplayClient\Data** directory and either rename or delete any files you find there to force QSR to reference the correct file path.

- Reapply DisplayClient Template in ControlPoint.


Once done DisplayClient should stay online.


**Long Term Fix**


As the VirtualStore folders are only created when a program is denied access to ProgramData, it is important to stress to customer that they most likely have some type of permissions issue with Windows and QSR. The customer should have their IT investigate as QSR does not manage permissions for customers. Until this is resolved there is no guarantee they will not have a similar issue again.