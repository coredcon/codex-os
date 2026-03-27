---
title: "TEXAS ROADHOUSE - Network Configuration / Could not determine Site Code"
freshdesk_id: 17000140239
category: "Support"
folder: "In Progress"
status: published
created: 2024-04-16
updated: 2024-07-05
views: 0
tags: ["CSK 2023", "QSR License Manager ", "Texas Roadhouse", "Site Code Error"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000140239
---

# TEXAS ROADHOUSE - Network Configuration / Could not determine Site Code

For reference, support ticket #358695.  

Error displayed when opening both QSR License Manager and ConnectSmart Registration, "Count not determine site code for this computer. Please contact QSR Support."

Short answer: This error was displayed due to their physical ethernet adapter (1 of 2) being disabled. 


Explanation, 
TXRH uses 3 network adapters, (2 Physical ethernet, 1 VM adapter).  

The QSR Server IP is statically assigned on the VM adapter however our software is looking at the physical adapters MAC which IPv4 was disabled thus causing this error to appear when opening ConnectSmart Registration and QSR License Manager.

Re-enabling the 3rd ethernet adapter with IPv4 will allow both programs CS Registration and QSR License to load successfully. 

It was mentioned adjusting the Advanced metric to 1 on the VM may help resolve if we did not enable the ethernet adapter but it is purposely set to 15 at their locations and with this being a live site we could not test.


Below is a image of the network adapters that are in use at a live location.  The adapter at the top of the list Broadcom NetXtreme Gigabit Ethernet is what we enabled to resolve.