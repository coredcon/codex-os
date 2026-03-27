---
title: "*|CSH| - ConnectSmart Host Server - Integration with Aloha"
freshdesk_id: 17000060019
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host Server - POS Integrations"
status: published
created: 2017-09-14
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000060019
---

# *|CSH| - ConnectSmart Host Server - Integration with Aloha

**ConnectSmart Host Server supports the following integration features with Aloha POS via the DineTime Aloha Client and either CSK or DineTime Kitchen Interface:**


**DineTime Aloha Client**


The DineTime Aloha Client interface uses the existing **ProHost*** interface built into Aloha to provide seven different functions (Dirty, Clear, Seat, Ordered, Check Printed, Payment, and Check Closed) that allow remote updates to the Host Client from an AlohaPOS terminal.


Aloha communicates via a text file that is dropped into a specific directory that ConnectSmart Host Server then processes.


The DineTime Aloha Client interface can be run on the same machine as ConnectSmart Host Server or on a separate machine. The interface reads from the ConnectSmartNetwork.xml in the Common\Data directory to obtain the IP address of ConnectSmart Host Server.


For installation instructions, see **DineTime Aloha Client User's Guide** found in the documentation folder included with the DineTime Installer.


*Make sure **ProHost **has been enabled in the Aloha configuration and pushed to POS clients