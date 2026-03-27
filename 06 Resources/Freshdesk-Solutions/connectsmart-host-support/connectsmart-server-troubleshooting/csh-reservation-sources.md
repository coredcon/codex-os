---
title: "|CSH| - Reservation Sources"
freshdesk_id: 17000139792
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Troubleshooting"
status: published
created: 2024-03-28
updated: 2024-03-28
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000139792
---

# |CSH| - Reservation Sources

Here is a breakdown of the relevant Visit Source enums supported in the API:


 


- **ConnectSmartKitchen** – visit originated in the ConnectSmart kitchen display application – e.g., there are options in the ConnectSmart Host Portal to create a new visit when a takeout or dine-in future order is started in ConnectSmart KItchen

- **QSR Enterprise ****AP**I – visit created via the Third-Party Enterprise API – e.g., you book a reservation using the API from your website or mobile app

- **ConnectSmart ****Host** – visit created in the ConnectSmart Host FOH client application (Windows)

- **ConnectSmart Host (iOS)** – visit created in the ConenctSmart Host iOS client application

- **ConnectSmart Host Portal** – visit created on the customer-facing ConenctSmart Host Portal web page

- **OpenTable** – visit created via the OpenTable-QSR partner integration from the OpenTable website or app

- **OnlinePartnerIntegration** – visit created via the Google Reserve or Wait List partner integration from Google search results/knowledge panel

- **_NULL_**** **– not certain how you would get a NULL value, so if you are seeing NULLs returned in the API, we may need to troubleshoot what is happening – that said, we do have a “NotSet” source in our enums to account for cases where the source is unavailable, but we’d need to peel that back as well to provide a specific reason why you’re seeing it


 


These are different than the report/dashboard labels used.  They do not match exactly to the strings used as enums for the API VisitSource field. 


 


For example, if you see “Enterprise API” on a report or graph, the source text string in the API would be “QSR Enterprise API”.  Google-sourced visits are returned in the API as “OnlinePartnerIntegration”.  The other sources are named for the QSR application where the visit was generated.