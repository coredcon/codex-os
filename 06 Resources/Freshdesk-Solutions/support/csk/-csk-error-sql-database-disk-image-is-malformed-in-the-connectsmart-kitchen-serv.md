---
title: "* |CSK| - Error 'SQL database disk image is malformed' in the ConnectSmart Kitchen Server Logs"
freshdesk_id: 17000115818
category: "Support"
folder: "CSK"
status: published
created: 2021-04-21
updated: 2022-12-08
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000115818
---

# * |CSK| - Error "SQL database disk image is malformed" in the ConnectSmart Kitchen Server Logs

**Issue:**


Speed of Service data is not available in Report Viewer, Kitchen Enterprise Reports, or via the API. While troubleshooting, the error "**(C:\ProgramData\QSR Automations\ConnectSmart\KitchenServer\Databases\SpeedOfService.db)- System.Data.SQLite.SQLiteException (0x80004005): database disk image is malformed**" is found in the ConnectSmart Kitchen Server logs. 


**Cause:**


The most likely cause is due to a corrupted SpeedOfService database. 


**Solution:**


  To resolve this issue please perform the following steps. 


-  First, stop the ConnectSmart Kitchen Service. 

- Navigate to the Database folder (**C:\ProgramData\QSR Automations\ConnectSmart\KitchenServer\Databases) **

- Locate the current Speed of Service DB and rename it to "SpeedOfServiceOld.db" 

- Restart the ConnectSmart Kitchen service.  Doing so will create a fresh database. 

- Review the ConnectSmart Kitchen Server logs to ensure the error is no longer populating. 


Unfortunately, the old data will no longer be accessible. However, reports and Speed of Service data should now be available moving forward.