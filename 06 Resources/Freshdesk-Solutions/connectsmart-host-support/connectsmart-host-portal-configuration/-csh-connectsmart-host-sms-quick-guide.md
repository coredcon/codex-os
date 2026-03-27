---
title: "* |CSH|  -  ConnectSmart Host SMS Quick Guide"
freshdesk_id: 17000086897
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host Portal / Configuration"
status: published
created: 2019-03-12
updated: 2022-12-12
views: 0
tags: ["DineTime", "SMS"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000086897
---

# * |CSH|  -  ConnectSmart Host SMS Quick Guide

Our SMS vendor is Twilio. Twilio logs are available to assist in tracking ConenctSmart Host SMS events if needed.


In order for the Messaging icon to present in the Host app when a Waitlist or Reservation party is selected the following must true:


1: SMS must be part of the Subscription package for ConnectSmart Host. 


2: Party must have a phone number in the Mobile Phone number field.


3: The Host app must be successfully connected to Cloud or Server (Green check). 


4: For Reservations, the Reservation date/time must be **the current business day**. You cannot manually SMS a future Reservation party until the day of the Reservation.


Message icon:


SMS can be sent automatically for certain events. (Example: Wait List Confirmation). Any SMS sent automatically from our Enterprise also show's up under the "Messages" icon in the Host client along with any manual SMS sent from Host and responses to SMS from customers.


Each SMS that Host can send automatically is configured in the Host Portal under the Concept (CONCEPTS >> TEXT MESSAGES). Make sure you are looking at the right concept for the site.


Most customers use the default SMS body we provide but we can enable fully customizable SMS 


configuration via a Concept level flag found in the Admin ([https://admin.qsr.cloud]).


Admin flag:


Which events we automatically send SMS for is also configured in the Host Portal but at the site level on a per site basis. Each site can determine which events a Concept level SMS will be sent by going to SITE >> CUSTOMIZE >> NOTIFICATIONS.


The only events we automatically send SMS to customers are defined in the Portal.