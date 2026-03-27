---
title: "*|Internal Only| - Orders are appearing in SocketMon, but not in the capture file"
freshdesk_id: 17000129468
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2022-11-10
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000129468
---

# *|Internal Only| - Orders are appearing in SocketMon, but not in the capture file

## Issue/Behavior:


This issue usually occurs when the NIC binding order of the QSR server network adapter and the POS server network adapter is not configured or is not configured correctly. 


## Resolution:


Open the Network Settings and click on Change Adapter Options -> Right click on the adapter -> Properties -> Internet Protocol 4 (TCP/IPv4) -> Advanced -> Uncheck automatic metric and assign the QSR server adapter interface metric to 1


Once you have done this it will be important to at least restart the CSK service or potentially the server if the issue persists.

Setting the Interface Metric to "1" will show CSK that this is the NIC that it needs to initialize with.