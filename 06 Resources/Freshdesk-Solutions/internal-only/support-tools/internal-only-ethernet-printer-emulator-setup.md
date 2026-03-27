---
title: "*|Internal Only| - Ethernet Printer Emulator Setup"
freshdesk_id: 17000131908
category: "Internal Only"
folder: "Support Tools"
status: published
created: 2023-03-08
updated: 2023-11-08
views: 0
tags: ["Ethernet Printer"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000131908
---

# *|Internal Only| - Ethernet Printer Emulator Setup

To configure Print Emulator:


Network & Internet Settings
Change adapters > IPV4 > Properties >(_IP should be static_)Advanced > add an unused IP address


 


 


Print Emulator executable


Create shortcut -> R click on shortcut -> At end of target path add
[SPACE][IP address you just added][SPACE]9100

 


Create new Ethernet Printer,  Assign it the new IP Assign it the correct Device ID from the dataset.
 


Restart ConnectSmart Kitchen Service
Run Print Emulator Shortcut
 IP address should be the same as IP for printer you added to ControlPoint