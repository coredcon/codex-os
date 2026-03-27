---
title: "*|CSH| - ERROR [0109]: Cannot create Web Browser control. One of its dependencies is missing. One or more errors occurred."
freshdesk_id: 17000058680
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Log Errors"
status: published
created: 2017-08-23
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000058680
---

# *|CSH| - ERROR [0109]: Cannot create Web Browser control. One of its dependencies is missing. One or more errors occurred.

**Issue: **


- Installing ConnectSmart Host Client by itself from Installer package > MSI folder

- Install _ConnectSmartHost.msi _

- Installs Successfully

- Errors out when launching the client


**Example ConnectSmart Host Client Log Excerpt:**


2017-07-06 16:46:53 ERROR [0109]: Cannot create Web Browser control. One of its dependencies is missing.


One or more errors occurred.


** **


**Resolution:**


- Close the client

- From the same version installer package > Redist folder

- Run _vcredist2012_x86_update4.exe_

- Re-launch client