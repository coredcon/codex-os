---
title: "*|CSK| - How to fix a CSK site that has registered with the wrong registration code"
freshdesk_id: 17000130162
category: "Support"
folder: "CSK"
status: published
created: 2022-12-12
updated: 2022-12-12
views: 0
tags: ["Server Registration"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000130162
---

# *|CSK| - How to fix a CSK site that has registered with the wrong registration code

## Issue/Behavior:


A site has accidentally registered with a registration code generated for a different site.


## Resolution:


- Stop the kitchen service

- Navigate to C:\ProgramData\QSR Automations\ConnectSmart\Common\Data

- Delete the DineTimeEnterprise.xml file and rename the MachineID.xml file to something different. 

- Register the site with the correct code and start the kitchen service.


**NOTE: If this happens to a DineTime/CS Host site depending on if the server has already synced the DT/Host data to its SQL DB then this may require you to uninstall DineTime/CS Host, uninstall the QSR01 instance completely, reinstall DT/CS Host which will create a new QSR01 Instance, and register the server with the registration code for the proper location.**