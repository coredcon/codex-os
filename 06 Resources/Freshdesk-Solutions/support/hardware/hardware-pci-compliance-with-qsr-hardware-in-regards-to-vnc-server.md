---
title: "*|Hardware| - PCI Compliance with QSR Hardware in regards to VNC Server"
freshdesk_id: 17000129432
category: "Support"
folder: "Hardware"
status: published
created: 2022-11-09
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000129432
---

# *|Hardware| - PCI Compliance with QSR Hardware in regards to VNC Server

## Helpful Information:


QSR controllers are staged with VNC Server, which may cause issues with PCI compliance/failed penetration tests. If the customer has concerns, here are some "best practice" standards that we recommend:


- Segment the controllers so that they are off the PCI network

- Set/rotate VNC passwords on the devices

- Completely disable VNC Server on the devices. There is a CE command-line tool that can disable VNC on xCeeds, and we may be able to write a bat file to disable VNC on eXperts.