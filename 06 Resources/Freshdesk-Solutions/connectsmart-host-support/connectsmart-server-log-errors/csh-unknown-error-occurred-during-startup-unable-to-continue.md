---
title: "*|CSH| - Unknown error occurred during startup, unable to continue."
freshdesk_id: 17000058679
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Log Errors"
status: published
created: 2017-08-23
updated: 2023-11-03
views: 0
tags: ["DineTimeServer", "Unknown Error"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000058679
---

# *|CSH| - Unknown error occurred during startup, unable to continue.

**Issue: **


**ConnectSmart Host Server fails to startup after install.  Error in logs:**


"Unknown error occurred during startup, unable to continue. View log for details.: System.IO.FileNotFoundException: Could not load file or assembly 'QsrLicenseInterop.dll' or one of its dependencies. The specified module could not be found."


**Solution**: 


The QsrLicenseInterop.dll is dependent on VC2015 runtime. However, VC2015 is dependent on specific Windows updates, so it is recommended that all users run Windows Updates prior to running the DineTime installer. This issue was caused by the VC2015 runtime installation being incomplete/corrupt because the target machine did not have the appropriate updates to support VC2015.


Reference: 
Ticket #117240