---
title: "* |CSH| - ConnectSmart Host Server - Full Uninstall/Reinstall including SQL"
freshdesk_id: 17000060150
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host - Installation and Application Management"
status: published
created: 2017-09-18
updated: 2024-01-24
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000060150
---

# * |CSH| - ConnectSmart Host Server - Full Uninstall/Reinstall including SQL

A normal Uninstall/Reinstall of the ConenctSmart Host Server will retain the local database and all of the configuration/historical data contained therein.  In some cases, it may be necessary to reinstall ConenctSmart Host Server with a completely blank database.  Examples include:


- Re-purposing an existing site's ConenctSmart Host Server to be used at a different restaurant

- ConenctSmart Host Server cannot launch because the database files are corrupt

- The site needs to roll back to an earlier version of the ConenctSmart Host Server than what is currently installed

- The incorrect site was registered to the server and the service was started. 


**Instructions:**


- **Uninstall ****ConenctSmart Host Server****: **Uninstall ConenctSmart Host Server  by launching the ConnectSmart Host installer and choosing Uninstall OR by choosing ConenctSmart from Programs and Features in the Control Panel and clicking Uninstall

- **Uninstall Microsoft SQL Server 2012/2016: **Once the ConenctSmart Host Serveruninstall is complete, uninstall the QSR01instance of Microsoft SQL Server 2012/2016

- Select **Microsoft SQL Server 2012 or 2016** from Programs and Features and click **Uninstall/Change**


-  A new window will open, Select **Remove** on the popover window 

- Wait for the Setup Support Rules operation to complete, and click OK


- Choose **QSR01** from the "_Instance to remove features from_" drop-down, and click **Next **


- Select the checkboxes under QSR01, leave the checkboxes under Shared Features unchecked, and click **Next  **

- Wait for Removal Rules operation to complete and click **Next **


- Click **Remove** on the Ready to Remove screen

- 

- Click **Close** when complete


Next,  you will need to Delete the SQL QSR01 database folder: Remove the database files from the SQL directory


- Navigate to** C:\Program Files\Microsoft SQL Server**

- Before deleting files, zip up the following folder and copy to a different path like the desktop or documents:
C:\Program Files\Microsoft SQL Server\**MSSQL11****.QSR01 or MSSQL13.QSR01  **

- Delete the above named folder contained within the **Microsoft SQL Server** directory

- **Reinstall ConnectSmart Host Server **using the installer

- If needed (if the wrong site was previously registered) Generate a new HOST **r****egistration code** from the portal and enter it into the **Registration tool**.  

- Start **ConnectSmart Host Server **and data will begin to sync down from Enterprise