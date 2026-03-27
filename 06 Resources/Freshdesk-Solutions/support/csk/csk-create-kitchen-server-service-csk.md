---
title: "*|CSK| - Create Kitchen Server Service (CSK)"
freshdesk_id: 17000049369
category: "Support"
folder: "CSK"
status: published
created: 2017-04-20
updated: 2022-12-08
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000049369
---

# *|CSK| - Create Kitchen Server Service (CSK)

**Issue:**


ConnectSmart Kitchen Server is not listed in the available services. 


**Resolution: **


In case the ConnectSmart Kitchen Server service  is missing, you can create it with the following command using Windows command prompt:


CSK 3.x:


**sc create "QSR ConnectSmart KitchenServer" binpath= "C:\Program Files (x86)\Qsr Automations\ConnectSmart\BackOffice\KitchenServer\CSKServer.exe"**


CSK 5+:


**sc create "QSR ConnectSmart KitchenServer" binpath= "C:\Program Files (x86)\QSR Automations\ConnectSmart\KitchenServer\Bin\KitchenServer.exe"**