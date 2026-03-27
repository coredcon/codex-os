---
title: "*|Internal Only| - Unable to connect to Zoho Unattended session - firewall error and need to restart a service or reboot server."
freshdesk_id: 17000124978
category: "Internal Only"
folder: "Remote Access"
status: published
created: 2022-04-29
updated: 2023-11-03
views: 0
tags: ["Zoho", "Restart Services"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000124978
---

# *|Internal Only| - Unable to connect to Zoho Unattended session - firewall error and need to restart a service or reboot server.

If connection states customer unable to join session or receive error about firewall:


Use the three dots on right of Unattended session link and select the Power Options or Diagnostic Tools you need.


I would first check to see if you can connect to Services (this saves you time and will help bring site up faster).


Example you are unable to connect and need to restart Kitchen Server service, can do so through Services link.


When the Services are not available or you need to restart the QSR Server box, select Restart, after a few minutes refresh your browser and you should be able to bring up Services, Device manager or any of the other options. 


You can stop start the service you need using the three dots at the end of the service.


**Note: **You can restart Zoho Assist-Remote Support service, but I have found this reboots the server, so you want to re-check QSR services afterwards to insure they are still running. 


**NOTE:**


If time is incorrect on QSR server the Unattended Zoho connection will error out with the whitelist message.
But when you try a manual Zoho connection at same site, zoho page will alert you that the connection can not be made because the time is wrong.
When this is the situation site's IT team see's it on line and we get the whitelist network error.
Resolve by correcting time and restarting Unattended Zoho connection.