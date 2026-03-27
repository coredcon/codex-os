---
title: "* |CSH| -  Unable to connect to your local server.  Check your network connectivity and ConnectSmart Host configuration"
freshdesk_id: 17000058934
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Troubleshooting"
status: published
created: 2017-08-29
updated: 2022-12-12
views: 0
tags: ["DineTime Host", "iPad Connectivity", "IOS", "DineTimeServer"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000058934
---

# * |CSH| -  Unable to connect to your local server.  Check your network connectivity and ConnectSmart Host configuration

**Description:**


Customer receives the following error when launching the ConnectSmart Host app on their iPad:


"Unable to connect to your local server.  Check your network connectivity and ConnectSmart Host configuration."


If customer is using the Standalone/IOS (Cloud) version of the app, see article in**Connectsmart**[** Host (Standalone/IOS) - Troubleshooting**]**:**


[Unable to connect to your ConnectSmart Host Server. Check your network connectivity and ConnectSmart Host configuration.]


**Troubleshooting:**


- Verify iPad is connected to Wi-Fi


        Settings -> Wi-Fi.  


        Make note of IP Address.


- Verify that the QSR ConnectSmart Server Service is running on the ConnectSmart Host  Server machine.

- Open **ConnectSmart Network Configurator** on ConnectSmart Host Server machine. Check that the Hostess Server IP matches correct ConnectSmart Host  Server IP.

- Verify the ConnectSmart Host settings on the iPad are configured properly to point at the ConnectSmart Host Server:


_Settings -> Host_


User Local ConnectSmart Server = Yes


Server = [ConnectSmart Host Server IP]


Port = 32776 _(assuming Base Port in ConnectSmart Network Configurator is 32768)_


Polling Interval = 1


Settings Polling Interval = 10


- Verify you can ping the iPad from the ConnectSmart Host Server machine.

- Verify the iPad is connected to the correct Wi-Fi (one that has a line of site to the Host Server IP).

- Verify the site has enough Host licenses to run the ConnectSmart Host Client.