---
title: "|Hardware| - Downgrading DisplayClient for a Windows Controller"
freshdesk_id: 17000140806
category: "Support"
folder: "Hardware"
status: published
created: 2024-05-03
updated: 2024-06-04
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000140806
---

# |Hardware| - Downgrading DisplayClient for a Windows Controller

Due to support for Edge browser, the most recent versions of DisplayClient won't run on Win7 or older Win10 devices. Customers who have upgraded to CSK 2023+ may see QSRDisplayClient.exe-System Error stating “**The program can’t start because MSVCP140.dll / VCRuntime140.dll is missing from your computer**.” on these older devices when they try to run DisplayClient.


 


To downgrade DisplayClient on these devices:


- Open current dataset in Builder and un-select Automatically upgrade display clients for Windows on Display Clients tab in Kitchen System Settings form. 


Select Tools>Copy Current to Runtime in Builder and restart the Kitchen Server Service before moving to the next step.


 


- Create the folder **Win32_2022** in this directory on the server: 
_C:\ProgramData\QSR Automations\ConnectSmart\KitchenServer\ClientInstalls\DisplayClient_


 


- Copy QSRDisplayClient.exe from a CSK 2022 installation to the newly created Win32_2022 folder.


- In ContolPoint, create a new Win32 2022 template and import this file into the Bin: 
_C:\ProgramData\QSR Automations\ConnectSmart\KitchenServer\ClientInstalls\DisplayClient\Win32_2022\QSRDisplayClient.exe_


 

- For affected devices, uncheck Win32 template and check Win32 2022 template on Templates tab of the station in ControlPoint and save.