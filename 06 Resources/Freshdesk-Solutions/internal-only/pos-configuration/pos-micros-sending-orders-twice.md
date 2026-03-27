---
title: "*|POS| - Micros Sending Orders Twice"
freshdesk_id: 17000129467
category: "Internal Only"
folder: "POS Configuration"
status: published
created: 2022-11-10
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000129467
---

# *|POS| - Micros Sending Orders Twice

## Issue/Behavior:


Orders being sent twice from Micros POS.


## Solution:


Here are some settings to check if Micros is sending orders to CSK twice.


- Make sure that they are using MicrosTsConnect version 2.0.33 (or later) with associated DLL and SIM (.isl) files.

- The "Check Info Print Format" in the Order Devices should be "After Header" rather than "Before Header".

- 


- All options in the Order Devices tab in the Order Types menu should be unchecked.