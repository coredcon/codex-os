---
title: "|CSK| - Addition of Site Code to KitchenServer.log - CSK 2024.1"
freshdesk_id: 17000138643
category: "Support"
folder: "CSK"
status: published
created: 2024-01-25
updated: 2024-01-25
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000138643
---

# |CSK| - Addition of Site Code to KitchenServer.log - CSK 2024.1

The site code is now written both during EOD processing and at startup. The log messages containing the site code also include the phrase "site code" so that it's easily searchable. When EOD is triggered, the site code is written almost immediately, so will be included in the log that gets archived:


```
2024-01-25T12:29:34.817-05:00,25892,28160,General,KitchenServer.cpp,1879,CKitchenServer::RunEndOfDay,Running End of Day 2024-01-25T12:29:34.831-05:00,25892,18352,Critical,KitchenServer.cpp,651,CKitchenServer::onActiveEndOfDay,Processing end of day for site code [63C4BA065B90F6EE]
```
The site code is then written again upon startup, so it will appear in the active log as well:
```
2024-01-25T12:29:37.265-05:00,25892,18352,General,KitchenServer.cpp,2227,CKitchenServer::startActiveServer,Starting Active Server for site code [63C4BA065B90F6EE]
```
Please note that the site code is written to the logs on both the primary and secondary servers, if you're using redundancy. However, only the site code from the primary logs is really useful, since that's the server that's registered to Enterprise. The secondary server does not know the primary's site code, so it logs its own site code (the site code that would appear if you opened License Manager on the secondary machine), even though that is not registered to Enterprise.