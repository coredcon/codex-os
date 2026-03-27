---
title: "|RecipesPlus| - Set up/configuration process for Recipes Plus"
freshdesk_id: 17000138483
category: "Support"
folder: "RecipesPlus"
status: published
created: 2024-01-17
updated: 2024-01-17
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000138483
---

# |RecipesPlus| - Set up/configuration process for Recipes Plus

**This article is a high level overview of the configuration involved with Recipes Plus**


- The initial administrator login for the Recipe Management portal is automatically created and credentials emailed to the administrator when the RecipesPlus subscription is added for as customer.

- Recipe data must be entered by one of the following methods:

- Manual entry (5-10 minutes per recipe)

- Import from TeamAssist 1.0 database (most customers will still want to touch each recipe to make small adjustments)

- Import via RecipesPlus API (direct integration with a partner or customer can build their own middleware)


- POS Item IDs must be mapped to their respective recipes in the MyConnectSmart portal (if using the CSK integration)

- If customer has variant menus or variant recipes specific to a subset of their sites, these need to be set up in MyConnectSmart portal and mapped to the sites.  If no menus are created, all recipes will show for all sites.

- CSK must be upgraded to 2023.7 or later.

- CSK configuration dataset needs to have RecipesPlus enabled for each station it will be used on, and a RecipesPlus View Role defined if they want the recipe to show specific steps for specific stations

- The following endpoints may need to be whitelisted in the customer’s firewall (port 443):

- RecipesPlus.qsr.cloud (if they do not have *.qsr.cloud wildcarded already)

- api.licensespring.com

- saas.licensespring.com


- The RecipesPlus Proxy needs to be installed on the back of house PC, which serves the following purposes:

- Stores the product license

- Allows DisplayClient to access RecipesPlus in the cloud even if the individual stations’ access to the outside internet is locked down

- Identifies the site to RecipesPlus so that the correct menu/recipes show for that particular site

- Provides security without requiring a login/password (a device must be on the store network with a line of site to the machine running the proxy in order to access the recipes)


- Run the RecipesPlus proxy as a process and it will prompt the user to enter the License Key and the site’s zip code.
 _Once the License Key has been entered, the customer can stop the process and run as a service if the prefer_