---
title: "*|CSH|- Mobile Device Management (MDM) configuration keys for DineTime, CS Host, Assist for iOS"
freshdesk_id: 17000058747
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host - Installation and Application Management"
status: published
created: 2017-08-24
updated: 2022-12-12
views: 0
tags: ["DineTime", "IOS", "DineTime Host", "MDM", "Mobile Device Management"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000058747
---

# *|CSH|- Mobile Device Management (MDM) configuration keys for DineTime, CS Host, Assist for iOS

**Mobile Device Management (MDM) configuration keys for DineTime, CS Host, Assist for IOS**


**use_local_hostess_server**
Default: FALSE


Type: BOOL


TRUE = DineTime Server; FALSE = DineTime Host (standalone IOS)


**server_preference**
Default: 192.168.1.100


Type: String


DineTime Server IP (if using DineTime Server)


**port_preference**
Default: 32776


Type: String


Leave as default unless base port has been modified to something other than 32768 in the ConnectSmart Network Configuration on the DineTime Server


**polling_interval_preference**
Default: 1


Type: String


Leave as default


**settings_polling_interval_preference**
Default: 10


Type: String


Leave as default