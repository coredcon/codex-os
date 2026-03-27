---
title: "*|CSK| - Registering a Secondary Server for ConnectSmart Kitchen"
freshdesk_id: 17000141303
category: "Support"
folder: "CSK"
status: published
created: 2024-06-03
updated: 2024-08-16
views: 0
tags: ["secondary", "Register"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000141303
---

# *|CSK| - Registering a Secondary Server for ConnectSmart Kitchen

With the increasing usage of Enterprise components in the QSR environment, it is important that Secondary servers are registered in the portal. This is required for Toast, Insights reporting, and the usage of many of our Webhooks and API’s to continue functioning when the site is in Backup.


To register the Secondary, go to Server Registration in the portal as normal, Choose Generate Kitchen Code, and then choose the Secondary Server radio option.


Generate the code, and enter it in the Connectsmart Registration tool under Kitchen on the Secondary Server. Choose Secondary in this tool as well, and then Register.


 


Restart the Kitchen Service. From this point on, the Secondary Server will remain in contact with the Enterprise services and everything should continue to function as expected when in Backup mode.


If there are any issues registering, troubleshoot as you normally would with any registration issues (Firewall, Wan MiniPorts, etc)