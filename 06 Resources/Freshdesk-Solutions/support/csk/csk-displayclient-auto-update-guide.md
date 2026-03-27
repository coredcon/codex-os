---
title: "*|CSK| - DisplayClient Auto Update Guide"
freshdesk_id: 17000063900
category: "Support"
folder: "CSK"
status: published
created: 2017-12-05
updated: 2022-06-21
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000063900
---

# *|CSK| - DisplayClient Auto Update Guide

This article will explain the requirements and setup needed to use the Auto Update feature in DisplayClient.


**Requirements:**


CSK version 6.1 +


DisplayClient version 1.2.101+


**Filepaths:**


When installed, KitchenServer puts the DisplayClients in the following paths:


**Win32**** - C:\ProgramData\QSR Automations\ConnectSmart\KitchenServer\ClientInstalls\DisplayClient\Win32**


**CE**** - C:\ProgramData\QSR Automations\ConnectSmart\KitchenServer\ClientInstalls\DisplayClient\CE\Arm**


**Android**** - C:\ProgramData\QSR Automations\ConnectSmart\KitchenServer\ClientInstalls\DisplayClient\Android**


**Builder Settings:**


With CSK 6.1+, the auto-upgrade behavior is a configurable setting in Kitchen Builder. On the System Settings form, there is now a DisplayClient tab. On that tab, the user can opt to allow Kitchen to manage upgrades for Android and/or Windows DisplayClients. Alternatively, leaving those settings unchecked means KitchenServer will never attempt to auto-upgrade any DisplayClients. 


In addition, the site must already have DisplayClient 1.2 on each device. If the template is using 1.1, you must manually update the template on the devices to include the 1.2 DisplayClient in order for it to update automatically in the future.


From that point on, to update the DisplayClient either run the KitchenServer installer for a newer version which will then place the latest Display Client in the correct folder, or manually drop the updated DisplayClient into the correct folder listed above under **Filepaths**. Kitchen will then handle updating the DisplayClient. Nothing needs to be done to ControlPoint to update DisplayClient versions.