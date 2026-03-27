---
title: "|General| SaaS License Expiration & Renewal"
freshdesk_id: 17000148212
category: "General"
folder: "FAQ"
status: published
created: 2025-09-24
updated: 2025-09-25
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000148212
---

# |General| SaaS License Expiration & Renewal

Here is a basic breakdown of how the AutoRenew license expirations are actioned in our Licensing Portal:


SaaS licenses require consistent Portal check-in to ensure the license remains up to date.


Expiration timelines:


-   60 days from creation - When a new license is created, the expiration date is set 60 days from creation date


-   Auto renew formula is Current Expiration minus 45 days. - An internal job runs every day and actions any licenses where the expiration date meets this criteria.


-   At time of Auto Renew, Expiration is extended 60 days - When the Auto Renew job executes on a license meeting the criteria, it updates the expiration date to 60 days from the current date.


Based on this, if the site is consistently checking in, the expiration date of the license that has synced to the server should never be less than 45 days from current day.