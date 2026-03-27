---
title: "*|ControlPoint| - Setting Up An HP Thin Client In ControlPoint"
freshdesk_id: 17000125323
category: "Support"
folder: "ControlPoint"
status: published
created: 2022-05-11
updated: 2022-12-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000125323
---

# *|ControlPoint| - Setting Up An HP Thin Client In ControlPoint

The first thing to note is that the HP Thin Client is considered Non QSR Hardware by ControlPoint


Non QSR Hardware will need to be licensed as such in ControlPoint so you will need to request the ControlPoint Non-QSR hardware component be added to your license when you request it from the Validation Team.


 


Once this is done and ControlPoint is configured and templates are built (Display Client), this will allow the created templates to show as a selection under the Templates tab for the device in ControlPoint. Created templates will NOT show for Non QSR Hardware devices if the license does not have Non QSR Hardware enabled for both ConnectSmart Kitchen and ControlPoint.  


The station will be built as a Win32 Device:


It will also use a Win32 DisplayClient template (C:\ProgramData\QSR Automations\ConnectSmart\KitchenServer\ClientInstalls\DisplayClient\Win32):