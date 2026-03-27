---
title: "*|CSK| - Confirming if Whitbread Site is Using Supported Version of CSK"
freshdesk_id: 17000139923
category: "Support"
folder: "CSK"
status: published
created: 2024-04-05
updated: 2024-04-05
views: 0
tags: ["Whitbread", "Beefeater", "Bar Block", "EoL"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000139923
---

# *|CSK| - Confirming if Whitbread Site is Using Supported Version of CSK

We only support Whitbread sites if the CSK 2019 SaaS or greater (or 2019 asset file with valid software maintenance).  Many Whitbread sites will show a SaaS subscription for CSK but are still on CSK 3. You will need to verify the actual product in use at site. Here is how to determine what version they are using.

**Confirm Salesforce Shows they have Supported License**


If they do not have a valid SaaS subscription for CSK or a Supported CSK Asset License with valid software maintenance send the corresponding canned response notifying they are using EoL product. This will most likely be the CSK 3 EoL canned response.


**If they have Supported License Check Admin for Last Check In Version**


Most Whitbread sites will have a SaaS subscription, but that does not mean they have upgraded from CSK 3. Look up the Site Code in Admin Portal and confirm they have a last check in that has them with a supported version of CSK. 


The example below shows a site with a Saas Subscription, but it is not validated, and Admin shows they have never checked in. This would point to them using CSK 3 still. 


**If you are unable to verify they are using a supported version of CSK ask for a screenshot of the QSR License Manger from the server showing a supported version of CSK before continuing any support requests.**