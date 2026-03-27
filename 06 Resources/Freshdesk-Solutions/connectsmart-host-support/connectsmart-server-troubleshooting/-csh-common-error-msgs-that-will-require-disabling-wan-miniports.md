---
title: "* |CSH| - Common error msgs that will require disabling WAN MiniPorts"
freshdesk_id: 17000080093
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Troubleshooting"
status: published
created: 2018-10-25
updated: 2025-08-07
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000080093
---

# * |CSH| - Common error msgs that will require disabling WAN MiniPorts

**Issue: **


The ConnectSmart Host logs contain the following errors: 


- **"****Error MachineOrProductNotRegistered"**


**
**


- **"ERROR [7004]: An error occurred attempting to locate DineTime Enterprise: The discovery service successfully returned a response, but there was no data." **


**Explanation: **


Enterprise registration is based on MAC address. The Registration Utility runs a query to pull available MAC addresses from the machine, takes the first address on the list (alphabetically), and sends that to Enterprise, where it is saved in the Polaris database. When Server tries to check in with Enterprise, it runs the same query and sends the full list of available MAC addresses, and if anything in that list matches what's in Polaris, Server is allowed to check in.


What may be happening is that the WAN Miniport MAC addresses are changing every day. So the MAC address used to register the product doesn't exist on the machine the next day, and therefore Enterprise prevents Server from checking in.  In order to resolve we need to disable the WAN Miniport adapter group and re-register the product.


**Steps to resolve:**


1: On the PC you wish to register, go to Control Panel > Device Manager.


2: Expand the Network Adapters listing and you should see several adapters that start with “WAN Miniport”.


3: Right-click on the all WAN Miniport adapter entries and select Disable. At the prompt, confirm you want to disable the device.


4: Once these adapters are disabled, register (or re-register) your QSR products as normal.


5: The product(s) should now be able to successfully check in with Enterprise. This action should only be needed one time.