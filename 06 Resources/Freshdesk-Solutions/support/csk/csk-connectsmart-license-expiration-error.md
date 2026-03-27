---
title: "*|CSK| -  ConnectSmart - License Expiration Error"
freshdesk_id: 17000133225
category: "Support"
folder: "CSK"
status: published
created: 2023-04-14
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000133225
---

# *|CSK| -  ConnectSmart - License Expiration Error

**ConnectSmart – License Expiration Error**


 The ConnectSmart Suite of products relies on a License file for product activation. Below are steps to take should you encounter a license expiration message on a kitchen station or in the ConnectSmart Host client. 


**ConnectSmart Kitchen: **


**Enterprise Connectivity Concerns:**


- If ConnectSmart Kitchen Server has lost its connection to Enterprise, you may encounter an error on your Kitchen Stations alerting you to a license expiration message. 


- With SAAS product subscriptions, the license file will not auto-renew and adjust the date if there are billing concerns or loss in enterprise connectivity. 

- The expiry message will appear once you’ve reached 30 days from license expiration. 


- When a user engages a function on the bump bar or interacts with a touchscreen, the expiry message will disappear until the Kitchen has been idle for about 10 min. 

- If you suspect that your site is no longer connected to enterprise due to Network connectivity, or loss of Site Registration please direct the customer to check the following.

- **Kitchen Check-ins report**:

- This report shows all sites under the company with a Kitchen subscription. The data includes the store ID, Site name, Address, Concept, Last Check-in, and Kitchen Version. 

- To Access the report, log into the **Kitchen Portal > Insight> Kitchen Check-ins**


- QSR Analysts are able to check the Admin Portal to verify the last check-in date. 

- Please keep in mind that the timestamp is in UTC.


- As a best practice, we recommend disabling the WAN Miniport Network Adapters from Device Manager as they’ve caused issues with site registration loss. 

- Also, as a best practice, we suggest setting the interface metric to 1, on the adapter the ConnectSmart Kitchen server uses to prevent binding order issues if multiple adapters are in use. 

- Check the Kitchen Server log for a message relating to “**Machine or product not Registered**” or "**Cert Revocation**" errors. 

- The logs are found in the following path **C:\ProgramData\QSR**** Automations\ConnectSmart\KitchenServer\Log**

- If the above errors are present, please attempt to re-register the product after applying the best practices steps and checking the whitelisting requirements. 

- Bounce the Kitchen Server Service. 

- Verify in the QSR License Manager that the License date has been updated for the product. 


  


**ConnectSmart Host:**


**Enterprise Connectivity Concerns: **


- If ConnectSmart Host Server has lost its connection to Enterprise, you may encounter an error on your Host Clients alerting you to a license expiration message. 


** **


- With SAAS product subscriptions, the license file will not auto-renew and adjust the date if there are billing concerns or loss in enterprise connectivity. 

- The expiry message will appear once you’ve reached 30 days from license expiration. 

- The message will remain onscreen until the date of the license is more than 30 days away. 


- If you suspect that your site is no longer connected to enterprise due to Network connectivity, or loss of Site Registration, **please check the following before reaching out to QSR Support. **

- **Host Check-ins report**:

- This report shows all sites under the company with a Kitchen subscription. The data includes the store ID, Site name, Address, Concept, Last Check-in, and Kitchen Version. 

- To Access the report, log into the **Host Portal > Insight> Host Check-ins**


- As a best practice, we recommend disabling the WAN Miniport Network Adapters from Device Manager as they’ve caused issues with site registration loss. 

- Also, as a best practice, we suggest setting the metric to 1, on the adapter the ConnectSmart Host server uses to prevent binding order issues if multiple adapters are in use. 

- Check the Kitchen Server log for a message relating to “**Machine or product not Registered**” or "**Cert Revocation**" errors. 

- The logs are found in the following path** C:\ProgramData\QSR**** Automations\ConnectSmart\HostessServer\Log**

- If the above errors are present, please attempt to re-register your product after applying the best practices steps and checking the whitelisting requirements. 

- Bounce the ConnectSmart Host Server. 

- Check the QSR License Manager to make sure that the license has been updated.