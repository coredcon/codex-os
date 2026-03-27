---
title: "*|POS| - Setting Up FUTURE POS To Send To QSR"
freshdesk_id: 17000098522
category: "Internal Only"
folder: "POS Configuration"
status: published
created: 2019-12-18
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000098522
---

# *|POS| - Setting Up FUTURE POS To Send To QSR

Client will first need to set up a QSR “printer” for the POS to speak with kitchen.

They do this in **System Devices**. When configuring the settings, the first instance where the port ID is requested, 7FFF was used successfully.

The remaining information is QSR standard settings (Server IP, port 32768, etc.) and Personal preference with the lay out of the POS information.


**Settings -> system devices -> QSR printer -> Settings**


Client will need to go to the **Back Office** -> **Settings** -> **System Settings**-> **Interfaces** -> **Kitchen VDU **and make sure that the “Process Modify Item Messages (When Available)” is **not checked**.


 


 


It’s also important to have QSRVDUDriver.exe running. It can be located C:FPOS5\Bin (Screenshot below)


It will show in the system tray once it’s up and going.