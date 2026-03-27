---
title: "*[Internal Only] - DISNEY SERVICES AND HOST SETUP"
freshdesk_id: 17000127197
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2022-07-13
updated: 2025-04-28
views: 0
tags: ["Disney ", "ConnectSmart Host", "DineTime"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000127197
---

# *[Internal Only] - DISNEY SERVICES AND HOST SETUP

This guide is intended to provide a general overview of how Disney and its affiliates utilize our current services. The hope is that this will aid support in any troubleshooting scenarios they may run across when dealing with Disney’s unique setup. 


 


**TABLE OF CONTENTS**


- Disney’s Subscription Services 

- Disney DREAMS

- D3 reporting/ Snowflake is the replacement for the D3 interface. 

- Additional Setup notes


 


Disney’s Subscription Services


Disney Parks and Resorts (**CID 2238**) Subscribes to ConnectSmart Host (**Product ID 215 in most cases with one-way SMS**) and a few APIs and Webhooks. 


 


Partner Development worked with Disney to set up the following services:


- GET - Visits by Loyalty Card ID (to support conflicts with other walk-up reservations) 

- POST - Guestbook record (if the loyalty ID card is not associated to any Host records) 

- POST WebAhead (Add webahead) API – to create the actual webahead reservation.

- POST – WebAhead Arrive API – to mark the guest as “checked-in” 

- POST – WebAhead Cancel API – to cancel the original webahead reservation in case there is a conflict. 

- PATCH – Reservation by visit ID API – to pass the custom values for the webahead reservation.


The Customer Project Transition doc can be found [here. ]


 


Disney also utilizes the **GET PrecalculatedQuotes webhook **(requires CSH server 2021.7.1) to get real-time quote information. This is used to engage a “Kill Switch” to stop guests from adding themselves to the waitlist once a 60-min quote time is reached in Host. **Disney prefers to fill their restaurants with reservations primarily. Then they will add any walk-ins that can be quickly seated.** 


 


 


Disney DREAMS


 


Disney **DREAMS** is the system Disney uses to manage in and off-park dining **reservations**. The DREAMS system **has its own Reservation Availability,** separate from the QSR Availability Plans for the specified store. You'll note that for the most part, Availability plans are not used in the Reservation settings in the Host Portal. 


Disney will send Reservations in a large batches of reservations in the early morning and then send new and updated reservations every 5 min. 


- The only way to book a reservation for a Disney store is through their “A La Carte” application. So, there shouldn’t be any reservations that come from other sources unless they are an affiliated store (a Disney operating partner) that may also take QSR online, OpenTable, Google Bookings, or in-store reservations. 


 


Note: The reservation record is added to the site Reservation Book in Host regardless of time slot availability. 


 


There are also, **non-Disney restaurants** (Disney Operating Partners) that will fall under the Disney Parks and Resorts company umbrella, but are not Disney owned and managed locations.  **They partner with Disney for the express purpose of being able to have access to the DREAMS reservations and some reporting.** There are a couple of important things to note:


- You can generally tell if they are only a Disney-affiliated site if the support request comes from a certain restaurant group (Patina Group, Bottleneck MGMT, etc.) and not from a @disney email. 

- They do not get access to the **Disney** **Guestbook, which is cleared every 30 days** per a script Disney Commissioned from us. 

- They must work with their Disney IT support contact if they did not get the daily Reservation batch push from DREAMS. The Disney IT team will then contact QSR support for any additional assistance that may be needed. 

- **Otherwise, please treat them like any other customer and troubleshoot their concerns as you would any other host user. **


 


Disney Custom Reporting 


 


The D3 interface, that QSR was commissioned to build, uses our API to pull the following information at the described intervals into their own data warehouse. ***** Disney recently rebuilt this application, and it is now called Snowflake****.** **QSR did not work with Disney or their contractors when this application was built****. This means that the data collected and intervals may have changed since the rebuild. *****


 


Support should not run into many cases to troubleshoot D3 (It was decommissioned in their production environment) or the Disney owned application "Snowflake", however, I have noted what data was collected in D3 below. 


The type of records collected are noted below:


 


**Record Types**


- Servers – Sent only once a day when new servers are added

- Tables – Sent Daily and on Table Status Change

- Meal Periods – Sent Daily and on meal period settings change

- Reservations – Sent when DREAMS reservation is loaded and updated

- Arrivals – Sent when DREAMS reservation guest arrives, or when a walk-in is added or is unable to be seated. 

- Paging Activity – Sent when the guest is paged.  

- Seated Data – Sent when a guest is seated or if the guest walks away after being seated. 

- Dirty Tables – Sent when tables are marked as dirty

- Clean Tables – Sent when tables are marked clean


 


 


- The visit events webhook enabled for their sites are the Party Seated, Arrived, and Notified. 


 


Additional Notes


 


- Disney runs a silent CMD line install that has on occasion contained Host Configuration XML files that can cause issues with some of the features not working as configured in the portal. To fix the config issues, resaving the information from the portal should do the trick. 

- The installation **script installs the QSR01 SQL database on a remote central database server**. So, it is important that should an issue arise that we have them check permissions to ensure line of sight to the host server. 

- They may have extra sites that aren’t being utilized that they will have spun up for new or different sites. Renaming of those sites should be handled by their AM (Kristine Gamble as of 04/2025) sending a request to Data Management. 

- They use Microsoft Azure for their Host Servers. Azure allows cloud hosting of VMs. 

- There are Self Service Kiosks available for Disney guests to add themselves to waitlists and Self-arrive their visits. These send an API call to add the visits to Host. These sites generally have a cloud subscription. 

- **They only use iOS clients in their stores.** However, there is a windows client accessible on the Server machine if troubleshooting from a windows client is needed. They will have to coordinate with a different area of their support team to get access to the Host server directly. 


*** This will be a living document and will be edited from time to time to keep up with known changes.***