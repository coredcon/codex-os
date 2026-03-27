---
title: "* |CSH| - WebAhead - Get Waitlist Status"
freshdesk_id: 17000061109
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host - Third-Party API"
status: published
created: 2017-10-09
updated: 2023-11-03
views: 0
tags: ["API", "WebAhead"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000061109
---

# * |CSH| - WebAhead - Get Waitlist Status

**Sample Call:**


[https://api.dinetime.com/Site/WebAhead/Status?siteUIDs=bf11d292-92d0-4605-9e65-4d50344a7582&partySizes=4]


**
**


**Sample Response:**


{


"SiteUID": "bf11d292-92d0-4605-9e65-4d50344a7582",


"WebAheadStatusId": 5,


"WebAheadStatus": "Available",


"Quote": {


"QuoteLow": 1,


"QuoteHigh": 5,


"SiteQuoteString": "5 minutes",


"ConsumerQuoteString": "About 5 minutes",


"ExactQuote": 5


},


"NumberWaitingVisits": 1,


"SiteId": 5848


}


**Possible WebAheadStatus** **Responses:**


- **Available**

- Site is online and accepting online wait-listing (i.e., WebAheads) at the time of the API request.


- **Disabled**

- Site has not been registered with Enterprise

- Site is currently offline (due to connectivity issue, or DineTime Server is not running)

- WebAhead has been disabled in the QSR backend settings (admin.qsr.cloud)

- WebAhead support at the site has been disabled using the “Disable WebAhead” API call


- **NotAccepting**

- Current time is outside of the site's configured operating hours

- WebAhead Availability is not enabled for the current Session


- **QuotingNotConfigured**

- This will only return if the site is polled during the QSR backend setup process.


- **DataNotReady**

- This will only return if the site is polled during the QSR backend setup process.


**
**


**Frequently Asked Questions:**


Official Documentation (Internal):


[https://qsrautomations.atlassian.net/wiki/spaces/GM/pages/382140516/WebAheadStatus]