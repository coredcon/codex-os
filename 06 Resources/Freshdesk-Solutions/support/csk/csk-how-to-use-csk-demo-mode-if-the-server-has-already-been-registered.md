---
title: "*|CSK| - How to use CSK Demo Mode if the server has already been registered"
freshdesk_id: 17000130163
category: "Support"
folder: "CSK"
status: published
created: 2022-12-12
updated: 2022-12-12
views: 0
tags: ["Demo Mode"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000130163
---

# *|CSK| - How to use CSK Demo Mode if the server has already been registered

## Issue/Behavior:


The client has already registered their server but there is not a license available yet and they would like to use Demo mode in the meantime. However, CSK currently will not allow you to go into Demo mode if the server has been registered because it's just trying to look for a license from the portal and will not start.


## Resolution:


- Navigate to C:\ProgramData\QSR Automations\ConnectSmart\Common\Data on the server and remove the "DineTimeEnterprise.xml" which will wipe out the registration.

- Start the Kitchen Server service and they should not be able to enter Demo Mode.


**NOTE: They will need to re-register again once their license is ready to be synced from the portal.**