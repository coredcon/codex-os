---
title: "*|CSH| - ERROR [6205]: Attempting to print active shift chit but no terminal settings match the specified Terminal ID of 'Default'"
freshdesk_id: 17000109469
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Log Errors"
status: published
created: 2020-09-25
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000109469
---

# *|CSH| - ERROR [6205]: Attempting to print active shift chit but no terminal settings match the specified Terminal ID of 'Default'

**Issue**:


When attempting to print, CommectSmart Host Server logs: ERROR [6205]: Attempting to print active shift chit but no terminal settings match the specified Terminal ID of 'Default'.


**Explanation**: 


This issue is caused by not selecting or writing a proper role on the Host clients.

**Solution**:
1. Select the correct terminal role from the Host clients
2. Write the correct role to HostessClientSettings.xml on each Host client and restart each Host client
3. Create a terminal role that matches the name they have configured currently in clients (Default)