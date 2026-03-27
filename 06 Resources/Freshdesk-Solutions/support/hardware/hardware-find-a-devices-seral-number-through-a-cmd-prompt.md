---
title: "*|Hardware| - Find a devices' Seral Number through a CMD prompt"
freshdesk_id: 17000137104
category: "Support"
folder: "Hardware"
status: published
created: 2023-10-13
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000137104
---

# *|Hardware| - Find a devices' Seral Number through a CMD prompt

**Find a devices' Seral Number through a CMD prompt**


Hopefully this can save Support some time when someone is having a hard time finding the serial number of a device.


Once have the serial number can verify with Team the device shows for the correct site.


**Example for ****HP-T640 Thin Client**


C:\Users\Admin>WMIC BIOS GET SERIALNUMBER


SerialNumber


MXL3142LB7


**Example for a laptop**


C:\Windows\System32>WMIC BIOS GET SERIALNUMBER


SerialNumber


R910BE7H


****


**
**


**
**


**Note: Be advised it is possible the serial number in the software may differ from the sticker and what we have on file.**