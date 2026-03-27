---
title: "*|CSH| - End of Day Changes in CSServer 2023.6"
freshdesk_id: 17000137572
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host - Installation and Application Management"
status: published
created: 2023-11-08
updated: 2023-11-08
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000137572
---

# *|CSH| - End of Day Changes in CSServer 2023.6

There are some changes being made with the End of Day process beginning with ConnectSmart Server 2023.6


Historically we’ve always done a single database backup during EOD, which occurred halfway through the process and didn’t provide much ability to troubleshoot in cases where you needed to see the state of the restaurant before EOD processing began clearing things. As of ConnectSmart Server 2023.6, the system will now create two database backups. The first is taken before any end of day processing occurs and the second after end of day completes.


 


To ensure that both backups can be saved to the same location, all database backup names will now be appended with “_BeforeEOD.bak” or “_AfterEOD.bak”. This holds true whether the restaurant is using the default name for the database or has configured it to save with a different name.