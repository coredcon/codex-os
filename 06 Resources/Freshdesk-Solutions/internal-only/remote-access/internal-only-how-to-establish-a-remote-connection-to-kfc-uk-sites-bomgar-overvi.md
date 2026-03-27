---
title: "*|Internal Only| - How to establish a remote connection to KFC UK sites (Bomgar) + Overview of common support requests"
freshdesk_id: 17000129472
category: "Internal Only"
folder: "Remote Access"
status: published
created: 2022-11-10
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000129472
---

# *|Internal Only| - How to establish a remote connection to KFC UK sites (Bomgar) + Overview of common support requests

When receiving a support issue regarding KFC in the UK you can remote into the sites via Bomgar.


 


Open your Bomgar Client application and enter your credentials:


 


 


***DISCLAIMER* The Bomgar client may update when you login if there has been a new version released**


 


 


Example email subject: "**Subject:** [EX] -UK11047RF Portsmouth Commercial Road KFC Additional KDS Install 19.12.18"


    - The site id will be - 11047 to search in Bomgar.


 


 


****All KFC site are listed in the DineTime Portal and if need you can use that as a resource to look up the site ID based on the address****


 


KFC Site IDs follow two guidelines:


    - Site IDs with 4 digits are corporate stores


    - Site IDs with 5 digits are franchise stores


 


 


Next we will discuss the difference between the KFC sites that use KDS and the others who use CSK 8:


 


**KDS**


 


**Dataset Standards:**


    - Fusion Flex EI – Eat in sites 6 stations + 1 order ready


    - Fusion Flex DT - Drive Thru 7 stations + 1 order ready


 


Some sites will have a unique setup that was built specifically for them - you will want to verify the stations being used via the dataset in KDS Builder.


 


**Windows Profile Credentials:**


    -Username: .\end21


    -Password: 82mass30


 


The KFC KDS sites will have a dedicated QSR Server. The naming convention used in Bomgar is UKXXXXRF_QSR (ex. UK11047RF_QSR)


 


**CSK**


 


KFC sites are now using portal datasets


 


CSK 8 Sites will have CSK running on the Back of House (BOH) computer. The naming convention used in Bomgar is UKXXXXRF_BOH (ex. UK11047RF_QSR)


 


When logging into a BOH you will need to log out of the staffs user account using the following steps:


- To log out of the BOH user account you will need to select Canned Scripts > General > Windows 7 login script. (see screenshot) This will log the user account out.


 


 


-To login to the BOH with the admin account use the following credentials:


    - **Username:** .\End21


    - **Password: **82mass30


 


**KFC Support Point of Contact as well as common support requests**


 


Fujitsu will be the main point of contact when needing to relay information back to the customer / YUM HO. Unless specified you will not need to contact a KFC site directly.


If a device is not functioning correctly and needs to be replaced, Fujitsu will log a call with engineers to complete the hardware replacement.


**    - Routing – **All routing is managed by YUM systems team. If there is an issue with routing of a particular item / items . This will need to be correct by YUM.


**    - MS2 DB **– There are two setups for MS2 DB which controls routing of items. (MS2DB = POS database)


            - KDS MS2DB


            - CSK MS2DB


Common issues with routing occur when a site is upgraded from KDS to CSK 8 and the MS2DB has not been updated to reflect the new changes. This will be managed by YUM systems team.