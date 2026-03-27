---
title: "*|Internal Only| - User Group Install Error For Sites Using a Non-English Version of Windows"
freshdesk_id: 17000129470
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2022-11-10
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000129470
---

# *|Internal Only| - User Group Install Error For Sites Using a Non-English Version of Windows

**Error message: "An error has occurred while applying security settings. Users is not a valid user or group." This could be a problem with the package or a problem connecting to a domain controller on the network. Check your network connecting and click retry or cancel to end install"  **


This issue appears to happen when trying to install software on a non-English version of Windows where it is looking for a certain user group called "Users" that does not exist.


We were able to fix this issue by using the following command in Command Prompt:


```
`net localgroup /add "Users"`
```