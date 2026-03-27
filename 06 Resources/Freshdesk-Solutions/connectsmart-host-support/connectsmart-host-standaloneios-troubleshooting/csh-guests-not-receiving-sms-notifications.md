---
title: "*|CSH| - Guests Not Receiving SMS Notifications"
freshdesk_id: 17000116240
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host (Standalone/IOS) - Troubleshooting"
status: published
created: 2021-05-05
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000116240
---

# *|CSH| - Guests Not Receiving SMS Notifications

**Problem Reported**


Site is reporting that a significant number of guests are not receiving our SMS notifications.


**Possible Causes:**


- Wireless carriers in the US and Canada have begun to crack down on SMS message filtering. Filtering is applied to protect mobile subscribers from spam and other forms of unwanted messaging. This filtering also has an algorithm to detect and block A2P traffic.  The SMS notifications from QSR's line of applications would fall into this A2P category.

-  Mobile providers such as AT&T, T-Mobile, and Sprint allowed companies to A2P 10DLC solution by allowing A2p messaging via long code to US recipients after first registering their phone numbers. Verizon did not participate, as they have their own A2P long code filtering algorithms. To allow our SMS traffic to flow to guests unblocked, a number of QSR customers participated in the A2P 10DLC registration project. 


 


- Another Cause to not receiving SMS notifications is if SMS is not part of the customer’s subscription.


 


**Resolution:**


- Verify that SMS is included in the customer’s subscription by checking SalesForce, Admin, and the [Solution Article] for Host subscriptions. If SMS is missing, please engage the customer’s AM to have that added to their package.

- If subscription is not part of the problem, please gather phone number examples and rough date and time when the SMS was sent, and a copy of the Host Server logs. Reach out to the Technical Projects team who will then research in Twilio and open a case if needed.