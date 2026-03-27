---
title: "|RecipesPlus| - RecipesPlus Troubleshooting Guide"
freshdesk_id: 17000142136
category: "Support"
folder: "RecipesPlus"
status: published
created: 2024-08-05
updated: 2024-08-07
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000142136
---

# |RecipesPlus| - RecipesPlus Troubleshooting Guide

As RecipePlus is a new product below are steps to take when troubleshooting issues customers report. At time of writing documentation for the product is still a work in progress so information may change.


**Verify Site has RecipePlus License**


After doing normal checks to verify site is on supported software and has SaaS or Software Maintenance, check if they have the RecipePlus entre in Salesforce.


After confirming it exists in Salesforce, check the actual Site Code to see if Recipes Plus is on the license. It will only be an option for CSK 2023 and up. If it was added recently please make sure that the license was properly synced afterwards.


**Verify Site is a Minimum of CSK 2023.7.12 and DisplayClient Version Applied in Template is up to Date.**


CSK 2023.7.12 is the minimum version supported. After confirming that please verify that version of DisplayClient in use on devices matches version installed with their version of ConnectSmart Kitchen.


**Make Sure Devices in Use Support the Current Versions of DisplayClient**


Older Devices that are not compatible with current releases of DisplayClient are not compatible with RecipePlus. Most common examples are the xCeed DE4100 and 4200 and eXpert DX3000 controllers.


**Confirm that RecipePlus Proxy is Installed, Licensed, and Running**


In order for RecipePlus Views to work the RecipePlus Proxy server needs to be installed. Once Installed it will need to be ran as an application for at least the first startup to go through licensing process. Please refer to the "ConnectSmart RecipePlus Proxy Installation Guide" attached at bottom of document.


Please Note that the guide has instructions for how to run the application as a service, **but until those steps are taken the Proxy must be ran as an application. **Will also note port used for proxy is offset from the ConnectSmart Network XML by 15. So **most customers would run RecipesPlus at port 32768 so (32768+15=32783). **


**Check ConnectSmart Network Configuration Has Correct IP for RecipePlus Proxy Server**


At bottom of Net**work Configuration tool is the spot where you assign what IP the RecipePlus Proxy is installed on. In most cases this will be same as ConnectSmart Network Primary Kitchen Server.**


**Kitchen Builder Settings**


In Kitchen Builder View Manager -> Recipe menu there is a dropdown for Recipe Source that needs to be set to RecipesPlus. The view type on the station needs to be a Recipe View as well.


**Known Issues:**


Currently a station with only a RecipesPlus view has crashed DisplayClient on Win32 devices in testing. Adding a tab to the station will stop it from crashing. 


If the home tab on a station is the Recipe View, then DisplayClient will display it as black screen until you switch to a different tab and then back. It then works until DisplayClient is restarted. Per JEdwards this has been seen on both Android and Win32 devices.


Ticket where both issue was discovered: [https://qsrautomations.freshdesk.com/a/tickets/371993]


**DOCUMENTATION NOTE:** There have been some changes since the documentaton was made so there may be some differences, mostly in relation to defaults. Updated documentation is in progress and will replace what is here when completed.