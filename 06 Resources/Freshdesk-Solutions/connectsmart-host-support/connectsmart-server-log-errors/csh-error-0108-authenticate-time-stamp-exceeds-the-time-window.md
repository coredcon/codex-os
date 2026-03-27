---
title: "*|CSH| - ERROR [0108]: Authenticate time stamp exceeds the time window."
freshdesk_id: 17000058682
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Log Errors"
status: published
created: 2017-08-23
updated: 2022-12-12
views: 0
tags: ["DineTimeServer", "Client Connectivity"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000058682
---

# *|CSH| - ERROR [0108]: Authenticate time stamp exceeds the time window.

**Issue: **


ConnectSmart Host Client machine’s system time is more than 5 minutes off of the system time on the ConnectSmart Host Server machine.


**Example HostessServer Log Excerpt:**


_ERROR [0108]: Authenticate time stamp exceeds the time window._


_Authenticate time stamp exceeds the time window._


_                                     at QsrAutomations.Gaia.Shared.Utilities.Communications.LocalServiceHelper.ValidateLocal()_


_                                     at QsrAutomations.Gaia.Managers.ServiceManagerClasses.CustomOperationInvoker.performInvocation(Object instance, Object[] inputs, Object[]& outputs)_


_ _


**Example HostessClient Log Excerpt:**


_2017-07-13 19:58:53 Connecting to DineTime Server..._


_2017-07-13 19:58:54 ERROR [0108]: The current system time is out of sync with the server system time by more than 5 minutes. Unable to connect to DineTime Server._


_ __ _


**Resolution:**


 Compare system time on the Server machine vs the Client machine, correct whichever is askew.  Client system time needs to be within 5 minutes of the Server, Server needs to be within 5 minutes of Enterprise global time. Make sure that the Time Zone is set correctly in the Company Portal for this site.