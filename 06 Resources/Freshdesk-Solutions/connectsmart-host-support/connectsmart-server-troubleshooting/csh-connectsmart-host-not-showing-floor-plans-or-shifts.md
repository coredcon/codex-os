---
title: "*|CSH| - ConnectSmart Host not showing Floor Plans or Shifts"
freshdesk_id: 17000127410
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Troubleshooting"
status: published
created: 2022-07-29
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000127410
---

# *|CSH| - ConnectSmart Host not showing Floor Plans or Shifts

## Issue/Behavior:


 


- Floor plans **and** Shifts are not showing in the ConnectSmart Host client even after verifying that Host is connected to Enterprise.


 


- The HostessServer.log contained the following log message:

```
"The sync queue specified FloorPlan no longer exists locally, removing from sync queue."
```

```
 
```


 

## Solution:


 


To resolve this issue the QSR01 SQL Instance must be removed and then repair the ConnectSmart Host Server Installation to rebuild the QSR01 SQL instance.
 
 **NOTE: In-depth instructions on how to remove SQL Instance and Re-install DineTime instructions (w/ pictures) can be found here**: [https://qsrautomations.freshdesk.com/a/solutions/articles/17000060150]


 


**Steps to remove the QSR01 SQL instance:**


- Stop the DineTime Server and QSR01 SQL Server services.

- Select Microsoft SQL Server 2012 from Programs and Features and click Uninstall/Change (if they are on a newer version of DT then it may be SQL server 2016.).

- Select "Remove" when prompted.

- Wait for the Setup Support Rules operation to complete, and click "OK".

- Choose QSR01 from the "Instance to remove features from" drop-down, and click "Next".

- Select the checkboxes under QSR01, leave the checkboxes under Shared Features unchecked, click "Next".

- Wait for the Removal Rules operation to complete and click "Next".

- Click "Remove" on the Ready to Remove screen.

- Click "Close" when complete.

- Navigate to "C:\Program Files\Microsoft SQL Server" on the server and remove the folder with "QSR01" in the name.


 


**Steps to repair ConnectSmart Host and restore the DB:**


- Select ConnectSmart Server from Programs and Features and click Uninstall/Change.

- Select "Repair".


 


Once the above steps have been completed you should be able to start the new QSR01 SQL Server and existing ConnectSmart Host Server services. When opening ConnectSmart Host you should be able to see the floorplans and shifts that are listed in the portal (once they have synced).


 


NOTE: It could take some time for ConnectSmart Host to sync all the data from the Enterprise since creating a new local SQL DB.


 


If only the floorplan image isn't showing please see the [**Unable to see the Active Floor Plan Image**] solution article.