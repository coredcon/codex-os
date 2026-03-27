---
title: "Secondary Kitchen Server at Sites Using CloudPOS"
freshdesk_id: 17000145972
category: "Support"
folder: "CSK"
status: draft
created: 2025-04-09
updated: 2025-04-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000145972
---

# Secondary Kitchen Server at Sites Using CloudPOS

To use a Secondary Kitchen Server with CloudPOS (Toast, Counter Solutions, Sweetgreen Gravy, etc.), the Secondary needs to be registered as a Secondary Server. As with sites using other POS solutions, the Secondary must be running at all times with line of sight to the Primary so that the Persistence database stays in sync.


How it works: As long as the active instance, whether that's the Primary or the Secondary, is registered to Enterprise, and CloudPOS is enabled for the site, that active instance will poll CloudPOS. The Kitchen Server stores the last message ID that it has received in Persistence.db, so it should not download the same messages more than once. Only the active Kitchen Server downloads messages. If a switchover occurs, the new active server should begin downloading new messages based on the last message ID received at the time of the switchover. One caveat is that there is a small but non-zero chance of duplicate orders at failover if that occurs while the Primary is in the middle of receiving and processing an order.


As with any change, we strongly recommend customers test in lab before deploying to a live site.


How to register a Secondary Kitchen Server: [https://qsrautomations.freshdesk.com/a/solutions/articles/17000141303]


How to set up a Secondary Kitchen Server: [https://qsrautomations.freshdesk.com/a/solutions/articles/17000127064]