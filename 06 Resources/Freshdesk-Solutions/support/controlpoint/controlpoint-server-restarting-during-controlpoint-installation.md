---
title: "*|ControlPoint| -  Server Restarting During ControlPoint Installation"
freshdesk_id: 17000117951
category: "Support"
folder: "ControlPoint"
status: published
created: 2021-07-14
updated: 2022-12-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000117951
---

# *|ControlPoint| -  Server Restarting During ControlPoint Installation

There are a few reasons why newer builds of ControlPoint force restart the server during installation. 


- There are other open QSR services that are running on the machine. 

- Please take the time to check and stop QSR services/ processes from running when upgrading or performing a fresh install of ControlPoint.


- The POS in use on the server is Digital Dining. 

- This POS calls QSR's  RDS.dll when running and thus also needs to be stopped during ControlPoint installation.


- Future POS credit card process and service named "Shift4 UTG2" can cause a reboot and may need to be stopped


Another program on the server is accessing one of the DLLs that the installation is trying to access, typically the RDS.dll:


Stop any POS software or antivirus software that you are able to stop while you run the ControlPoint installation.


As a last resort you can boot the server into safe mode to ensure that nothing is running on the server before you run the installer.


This process will be different depending on the server.


** More to be added to this article, as new information is available. ***