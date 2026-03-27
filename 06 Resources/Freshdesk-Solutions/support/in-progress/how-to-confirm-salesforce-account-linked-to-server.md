---
title: "How to Confirm Salesforce Account Linked to Server"
freshdesk_id: 17000142372
category: "Support"
folder: "In Progress"
status: published
created: 2024-08-26
updated: 2024-12-12
views: 0
tags: ["Salesforce", "site code", "License"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000142372
---

# How to Confirm Salesforce Account Linked to Server

In some situations where multiple accounts exist at the same address it may be helpful to confirm what salesforce account is linked to the site you have remote access to. This can be as simple as looking up the Site Code if it has a license attached, but if the issue is the site is not licensed then it may be necessary to dig further. Below are things to look at.


**Look up Site Code in LMTS**


If the site has a license file attached you can look it up at [https://lmts.qsr.cloud/signin]


If it does have a license it will have the Lic# which can be searched in Salesforce and will take you to the account.


**Find the Site ID in the Kitchen Server Log**


In newer releases of CSK the Enterprise Site Info will list what Site ID the license was registered with. This can be searched for in Salesforce to find the site.


**When Comparing Multiple Possible Accounts Find Unique Identifiers in their Configuration**


If the steps above fail you will need to find something that will be specific to one site if possible. This can be the number of stations it has on license, or version of CSK it uses. You can then compare it to the Kitchen Server Log.