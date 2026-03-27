---
title: "*|Networking| - TLS 1.2 Support for DineTime/ConnectSmart Host Server"
freshdesk_id: 17000080011
category: "Support"
folder: "Networking"
status: published
created: 2018-10-24
updated: 2022-11-10
views: 0
tags: ["TLS", "Encryption", "SSL", "SQL Server"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000080011
---

# *|Networking| - TLS 1.2 Support for DineTime/ConnectSmart Host Server

**Issue: **


DineTime/ ConnectSmart Server currently supports TLS 1.2 encryption for Enterprise communication.  However, as of DineTime 6.4.106.0, the version of SQL Server packaged with the DineTime installer requires TLS 1.0.  Because of this, as customers make changes to disable SSL 3.0 / TLS 1.0 on their networks, they may encounter issues with SQL Server (and by extension, DineTime, since DineTime Server is dependent on SQL Server)


**Resolution: **


Development has confirmed that SQL Server 2016 included with DineTime Server 7+ will support TLS 1.2.  However, the TLS 1.2 compliant SQL Server version will only automatically upgrade if it is a fresh install of DineTime.  If the customer is upgrading from an earlier version they will need to launch the SQL Server installer manually for the correct version to be installed.


Customers experiencing the issue now can go ahead and download/install a TLS 1.2 supported SQL Server build from Microsoft.  The first build to support TLS 1.2 are listed here:


[https://support.microsoft.com/en-us/help/3135244/tls-1-2-support-for-microsoft-sql-server]


The current SQL Server version can be found in the SQL logs stored here: 


C:\Program Files\Microsoft SQL Server\MSSQL11.QSR01\MSSQL\Log


**Additional information: **


[How to enable TLS 1.2 on site servers and remote site systems]


**Why is TLS 1.2 Compliance Important?** Here at QSR Automations, our intention is to continuously deliver solutions that work to meet the requirements of the most security-sensitive organizations. In order to align with the technology and regulatory standards for Transport Layer Security (TLS) we will be updating the TLS configuration for all enterprise endpoints to a minimum of version TLS 1.2.  **We will be disabling all TLS 1.0 and TLS 1.1 communication to and from our Enterprise endpoints on March 15, 2023**. This will impact all users on CSK 5 - 7.3.107 and DineTime 5, as these versions are NOT compatible with the TLS 1.2 communication protocol and therefore not compliant with current security requirements.