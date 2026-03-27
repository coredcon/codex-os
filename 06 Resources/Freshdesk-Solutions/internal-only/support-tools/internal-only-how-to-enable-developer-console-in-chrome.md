---
title: "*|Internal Only| - How to Enable Developer Console in Chrome"
freshdesk_id: 17000138146
category: "Internal Only"
folder: "Support Tools"
status: published
created: 2023-12-14
updated: 2024-05-30
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000138146
---

# *|Internal Only| - How to Enable Developer Console in Chrome

When we forward issues to GravityCx they are going to need the HAR log and the Console Log found in the Developer Tools in Chrome. **The console needs to already be open before you have a error so this should be done in the morning and needs to be opened from the tab with Twilio Flex. **The console is found by selecting the three dots in the top right corner of chrome and then selecting More Tools -> Developer Tools.


Once the Console is open, navigate to the Network Tab and make sure the Preserve Log option is checked. You can then set the console to run in a seperate window by selecting the first Dock Side option on the left. 


If no issues occur then nothing more needs to be done. If you do run into a problem you will need to save the Console log and the Network HAR log.


**Saving Logs**


To save these logs, Right Click on any of the entries in the Console Tab and select "Save". Then do the same in the Network Tab and select "Save all as HAR with Content".