---
title: "OLO orders not showing on screens - Aloha POS"
freshdesk_id: 17000140805
category: "Support"
folder: "In Progress"
status: draft
created: 2024-05-03
updated: 2024-05-03
views: 0
tags: ["OLO", "Aloha POS", "OLO Orders not routing"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000140805
---

# OLO orders not showing on screens - Aloha POS

If OLO orders are not routing from Aloha POS check that the WAN mini ports are disabled.


**Step 1: 
**Search for "Device Manager".

**Step 2:
**Once the device manage window is opened, check that "show hidden devices" is selected by clicking View > Show hidden devices.


**Step 3:**
Expand the Network Adapters listing and you should see several adapters that start with “WAN Miniport”.
**
****Step 4:
**Right-click on the all WAN Miniport adapter entries and select Disable. At the prompt, confirm you want to disable the device.


Once you confirm the WAN miniports are disabled, restart the primary Kitchen server service and also restart the secondary Kitchen server service to confirm the primary Kitchen server has taken over and test if the OLO orders are now showing up, if the issues still persist and OLO orders are not showing up an Aloha refresh may be necessary.