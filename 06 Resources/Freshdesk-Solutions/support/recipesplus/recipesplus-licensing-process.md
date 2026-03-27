---
title: "|RecipesPlus| - Licensing Process"
freshdesk_id: 17000138482
category: "Support"
folder: "RecipesPlus"
status: published
created: 2024-01-17
updated: 2024-01-17
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000138482
---

# |RecipesPlus| - Licensing Process

**This article covers the high level steps involved with licensing Recipes Plus**


- The RecipesPlus subscription (product code: 001-7830) is added to the site in Salesforce

- The automation for our new licensing system will pick up the change and automatically create the license in our new licensing platform.

- An automatic alert is sent to the Validations team who will turn on the RecipesPlus feature flag in the LMTS license
 _This is only required if the customer wants to use the CSK integration with RecipesPlus_

- Run the RecipesPlus proxy as a process and it will prompt the user to enter the License Key and the site’s zip code.

- In the event of a server swap, MyConnectSmart will have a self service option for a customer/reseller to reset the validation without having to contact QSR.