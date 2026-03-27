---
title: "*|CSK| - Enterprise Check-In Results in 400: Bad Request Log Error"
freshdesk_id: 17000139806
category: "Support"
folder: "CSK"
status: published
created: 2024-03-30
updated: 2024-08-16
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000139806
---

# *|CSK| - Enterprise Check-In Results in 400: Bad Request Log Error

**Issue:**


The registration process is successful, but CSK does not check in when the service is restarted, and the following error is present in the KitchenServer.log:


Critical,EnterpriseServicesClient.cpp,181,EnterpriseServicesClient::MakeRequest,Failed to extract response data for request GET https://service-discovery.qsr.cloud/v1/stacks?ProductIdentifier=Kitchen&ProductToken=73640e38-a741-400b-9d88-e93796640a52&ProductRole=1: 400 Bad Request


**Workaround:**


Development is still researching a fix, but they have offered a workaround in the meantime.


1. Generate a registration code in the Admin portal for the site.


2. Open Command Prompt (run as Admin).


3. Type cd C:\Program Files (x86)\QSR Automations\ConnectSmart\Common\Bin and hit enter.


4. Run ConnectSmartRegistration.exe RegistrationCode Kitchen /pm (where “RegistrationCode” is the code you just generated).


5. Open DineTimeEnterprise.xml and verify that the Kitchen product has both an EnterpriseToken and EnterpriseID


6. Once the registration is complete and the EnterpriseID exists in the DineTimeEnterprise.xml, restart KitchenServer and review the logs to ensure it was able to successfully check in with Enterprise.