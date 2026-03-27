---
title: "*|Internal Only| - Disabling Wan Miniports for Registration Issues"
freshdesk_id: 17000086418
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2019-02-27
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000086418
---

# *|Internal Only| - Disabling Wan Miniports for Registration Issues

If a site is having issues registering in portal and it does not appear to be a license issue or an issue with the registration itself try the following:


From the QSR server,  open Windows PowerShell and run the following command:


**Get-WmiObject Win32_NetworkAdapter | where {$_.PNPDeviceID -notlike 'root\*' -and $_.AdapterTypeID -in (0, 9)} | sort MACAddress | select Name,MACAddress**


You will get something like this:


If the WAN Miniports are listed BEFORE the Ethernet adapter then Try the following.


There are a series of "WAN Miniport" entries that are shown when you run "Device Manager" in Windows.


We would like you to perform the following steps:


- On the QSR server, navigate to the Control Panel > Device Manager


- Expand the Network Adapters listing and you should see several adapters that start with “WAN Miniport”


(If these ports are not visible, go to the View menu at the top of the Device Manager window and select “Show hidden devices”)


- Right-click on the all WAN Miniport adapter entries and select Disable. At the prompt, confirm you want to disable the device


-Once all WAN Miniport adapter entries are disabled, register (or re-register) your QSR products as normal and restart all QSR services.