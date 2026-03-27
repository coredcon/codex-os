---
title: "When Deliveroo Tablet is not sending orders to QSR"
freshdesk_id: 17000142850
category: "Support"
folder: "In Progress"
status: draft
created: 2024-09-30
updated: 2024-09-30
views: 0
tags: ["#Deliveroo"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000142850
---

# When Deliveroo Tablet is not sending orders to QSR

**Scenario:**
Site is blaming QSR for Deliveroo Tablets not sending orders when they are able to send them from the POS stations to QSR Capture and screen.


**Troubleshooting Steps:**

 1. Validate that the Orders are not coming through the Deliveroo Tablet. This can be done by requesting the site to place a test order and provide the Order number. 


  2. Use Unattended Access (If available) to obtain the Capture log after the test has been ran, and confirm that the new order did not route to either  kitchen station.


  3. Validate that the Order's transaction number does or does not appear within the Capture log to rule out any issues pointing to an implementation adjustment needed for the Dataset.


  5. If the order does not show up within the Capture log advise the site to contact their Deliveroo Tablet Support team.


   (The Deliveroo platform needs to be integrated with the Site location ID from Zonal/Comtrex in order for it to send orders to QSR.)


Ticket Reference: [https://qsrautomations.freshdesk.com/a/tickets/359899]