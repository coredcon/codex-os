---
title: "* |CSH| - ERROR [7004]: An error occurred attempting to locate DineTime Enterprise: The discovery service successfully returned a response, but there was no data."
freshdesk_id: 17000077837
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Log Errors"
status: published
created: 2018-09-06
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000077837
---

# * |CSH| - ERROR [7004]: An error occurred attempting to locate DineTime Enterprise: The discovery service successfully returned a response, but there was no data.

**Issue: **


ConnectSmart Host Server will not connect to Enterprise and the following errors are shown in the HostessServer.log:


2018-08-30 17:52:59 ERROR [7004]: An error occurred attempting to locate DineTime Enterprise: The discovery service successfully returned a response, but there was no data.


2018-08-30 17:52:59  INFO [7007]: Enterprise discovery has failed: Falling back on default DineTime Enterprise services


2018-08-30 17:52:59 ERROR [7002]: An error occurred attempting to authenticate with DineTime Enterprise:


**Solution**: 


This error means the same thing as the "MachineorProductNotRegistered" error we often see when one of the following registration issues is occurring:


- The site is not registered

- Bad MAC Address

- Wrong Token

- Another site was erroneously registered to the site in question


Re-registering using a newly generated ConnectSmart Host Registration Code will most likely fix the issue, but it would be advisable to research how they got into this state.  If the MAC Address on the Server machine is changing at random, additional steps may need to be taken to ensure the site doesn't continue to lose connectivity.