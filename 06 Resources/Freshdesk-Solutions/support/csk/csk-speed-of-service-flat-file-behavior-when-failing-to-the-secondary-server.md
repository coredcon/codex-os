---
title: "|CSK| - Speed of Service Flat File Behavior when failing to the Secondary Server"
freshdesk_id: 17000130039
category: "Support"
folder: "CSK"
status: published
created: 2022-12-07
updated: 2022-12-07
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000130039
---

# |CSK| - Speed of Service Flat File Behavior when failing to the Secondary Server

Currently in CSK 5+ if the primary Kitchen Server fails over to the backup and the site is using the Speed of Service flat files then for that particular day that the server operated on the secondary the site will have to manually retrieve the flat file from the backup server Speed of Service directory.


**Example of the default Speed of Service directory: **_C:\ProgramData\QSR Automations\ConnectSmart\KitchenServer\SpeedOfService_


**Example(s) of KitchenServer.log entry showing where the server failed to the secondary:**


**                            **_(In this entry is where the server switched from operating on the primary server to the secondary server, and from this point till it switches back to primary the Speed of Service flat file with be located on the                                                             secondary server)_


****                            _(In this particular case the server had already failed over to the secondary but when processing end of day it switched back over to the primary, but for the Speed of Service file will be located on the backup for that day.)_