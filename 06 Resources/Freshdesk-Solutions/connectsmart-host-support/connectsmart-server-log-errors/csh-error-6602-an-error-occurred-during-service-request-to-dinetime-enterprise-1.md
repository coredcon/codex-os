---
title: "*|CSH| - ERROR [6602]: An error occurred during service request to DineTime Enterprise: [103] AuthenticationTimeOutOfRange"
freshdesk_id: 17000058681
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Log Errors"
status: published
created: 2017-08-23
updated: 2022-12-12
views: 0
tags: ["DineTimeServer", "Enterprise Connectivity"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000058681
---

# *|CSH| - ERROR [6602]: An error occurred during service request to DineTime Enterprise: [103] AuthenticationTimeOutOfRange

**Issue: **


ConnectSmart Host Server cannot connect to Enterprise because the system time on the ConnectSmart Host Server machine is more than 5 minutes off from the Enterprise Server.


**Example Log Excerpt:**


**_ _**_2017-07-13 01:47:54 ERROR [6602]: An error occurred during service request to DineTime Enterprise: [103] AuthenticationTimeOutOfRange_


_2017-07-13 01:47:54 ERROR [6602]: Failed to check-in to DineTime Enterprise:  ErrorCode: 103 - AuthenticationTimeOutOfRange_


_2017-07-13 01:47:55 ERROR [7005]: An error occurred attempting to locate DineTime Enterprise: The discovery service returned information about multiple enterprise stacks._


_2017-07-13 01:47:55  INFO [7007]: Enterprise discovery has failed: Falling back on default DineTime Enterprise services_


_ _


**Resolution:**


Check portal settings to insure time zone is configured correctly


- Login to portal ( portal.dinetime.com )

- Sites > Select your site > Manage > Restaurant Profile > Scroll down to “Time Zone”

- Check time and time zone on the machine running DineTime Server to make sure it matches the time frame set in the portal.


 Note: If it applies, check the box to adjust for Daylight Savings Time