---
title: "*|CSK| - Running a Silent Install"
freshdesk_id: 17000049364
category: "Support"
folder: "CSK"
status: published
created: 2017-04-20
updated: 2022-06-20
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000049364
---

# *|CSK| - Running a Silent Install

**Silent Installs**


You can run a silent install/upgrade on CSK. The following is a sample command-line parameter to silently install/upgrade CSK:


• **KitchenServerSetup.exe /q InstallKitchenServer=1 InstallBinEditor=1 **


*Note: Setting them to =0 instead of =1 will not install  that particular component.


**Silent Installs Commands**


•


InstallKitchenServer=<0,1> : command line param to control installation of KitchenServer (Default Value=1)


•


InstallBinEditor=<0,1> : command line param to control installation of BinEditor (Default Value=1)


•


InstallCrystalReports=<0,1> : command line param to control installation of the Crystal Reports


runtime engine (Default Value=1)


•


**Command Line Product Registration **


Command line product registration can be performed during a silent install. 


Enter the following command line parameters:


-      EnterpriseRegistrationCode="Registration code"

-  The registration code is generated here: SitePortal | Manage| Server Registration.


-      RegistrationCommand="Kitchen"


*Note: Type in “KitchenServerSetup.exe /help” to display a list of relevant switches:


With Controlpoint you should be able to simply use a /s flag for silent for both the server and the client