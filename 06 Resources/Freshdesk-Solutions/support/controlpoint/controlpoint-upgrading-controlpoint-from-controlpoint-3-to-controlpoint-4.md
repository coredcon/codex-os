---
title: "*|ControlPoint| - Upgrading ControlPoint from ControlPoint 3 to ControlPoint 4+"
freshdesk_id: 17000123357
category: "Support"
folder: "ControlPoint"
status: published
created: 2022-02-15
updated: 2022-12-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000123357
---

# *|ControlPoint| - Upgrading ControlPoint from ControlPoint 3 to ControlPoint 4+

**Stop ALL QSR services:** 


- If the POS in use on the server is Digital Dining. This POS calls QSR's  RDS.dll when running and thus also needs to be stopped during ControlPoint installation.


- If the POS in use on the server is Future POS and Future credit card process and service named "Shift4 UTG2" needs to be stopped during ControlPoint installation. 


**Note:** [https://qsrautomations.freshdesk.com/a/solutions/articles/17000117951]


Copy the following ControlPoint folders before fully uninstalling ControlPoint 3


C:\ProgramData\QSR Automations\ConnectSmart\**ControlPointClient\Data**


C:\ProgramData\QSR Automations\ConnectSmart\**ControlPointServer\Data**


C:\ProgramData\QSR Automations\ConnectSmart\**ControlPointServer\Templates**


C:\ProgramData\QSR Automations\ConnectSmart**\ControlPointServer\TemplateUpdates**


Once saving the folders off from ControlPoint Client and Server, **uninstall ControlPoint 3 Client and Server.**


**Delete all of the ControlPoint folders from ProgramData and Program Files (x86) directories.**


Install new ControlPoint Server and Client


Copy the saved data to the corresponding folders in ControlPoint Client and Server.


Run ControlPoint Builder and set as XML and save. (Some sites may set differently)


Double check the Network configuration to make sure ControlPoint is still checked with the correct IP.