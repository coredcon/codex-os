---
title: "*|Hardware| - Disable Edge UI on Windows All-In-One"
freshdesk_id: 17000052381
category: "Support"
folder: "Hardware"
status: published
created: 2017-05-31
updated: 2022-08-02
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000052381
---

# *|Hardware| - Disable Edge UI on Windows All-In-One

**(Added regedit file attachment that will make this change as well. Run, "ok","ok", reboot)**


In some cases, an All In One may have the ability still enabled that allows a user to swipe from the edge of the screen and minimize the display. Below are the steps to disable that manually.


1. Open Group Policy Editor. You can do this by opening the Search bar and typing Edit Group Policy:


2. In the menu to the left, go to Administrative Templates>Windows Components>Edge UI


3. Double click on "Allow edge swipe" in the right window. The Editor window will open. 


Choose Disabled and click OK:


4. Reboot the device. 


Once the device has rebooted, the user should no longer be able to swipe from the edge and minimize the display.