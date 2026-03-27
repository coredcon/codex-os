---
title: "Troubleshooting the OpenTable Integration"
freshdesk_id: 17000141072
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host Partner Integrations"
status: published
created: 2024-05-16
updated: 2024-05-16
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000141072
---

# Troubleshooting the OpenTable Integration

**Troubleshooting the OpenTable Integration**


 


QSR has two different WebAhead (online waitlisting) and Reservation partner integrations. Customers may call in because they are facing challenges with either getting availability from ConnectSmart Host or the integration working at all. This document will outline the most common issues and how to troubleshoot them.


 


**OpenTable is not showing any Availability**


If a customer calls in and indicates that they should have the OpenTable integration enabled, but they aren't getting and Availability. Please check on the following settings. 


- First, you will need to verify that the integration has been enabled for that site.

- Navigate to the **Admin Portal** ([https://admin.qsr.cloud])

- Search for the Site

- From the menu on the left, Expand the** Partner Settings** menu and then go to **Site Partner Settings**.

- Scroll Down to look for **OpenTable**

- This setting should be checked and with a **Partner Site ID** that was supplied directly from OpenTable. 

- If the Active Flag is unchecked and there is no Partner ID, then Technical Projects has likely not received an email from the OpenTable integration specialists to activate the integration. Please direct the customer to work with their OpenTable account manager to get the ball rolling. 

- 


    2.  The OpenTable integration also requires its **Visit Source** to be enabled.     


- From the **Partner Settings** Menu, Select **Visit Source**.

- Pay Attention to whether **Concept Settings** are being used, If so, please navigate to the **Concept level settings**. 

- Verify if the **Web Reserve Status** is set to **accepting**. If not, then please reach out to the Technical Projects team to adjust this for you. 


    3.  If the integration is enabled and further troubleshooting is needed, you will need to also check the **WebAhead settings**. 


- Navigate to the **Admin portal**.

- Search for the affected site.

- Expand the **Site Settings** menu on the side. 

- Click on **WebAhead Settings**. 

- Please note that the first line under **Visit Source is a dropdown menu**. 

- Verify if the site is using Concept Settings. If so, navigate to the concept level settings that this site is located under. 


- Select **Online Partner Integration** from the drop-down menu and verify. 

- That Web Reserve Status is set to Accepting for OpenTable


- If that is set to Not Accepting, please reach out to the Technical Projects team to enable.   


    4. If this still does not resolve the issue, you will want to check the Host Portal for a few settings. 


- Navigate to the **Host Portal** ([Https://Portal.Host.qsr.cloud]) 

- Go to sites and choose the affected site

-  Then go to **Floor Plans** and then **Seating Areas**

- Scroll down to the Reservation Availability Types and ensure that, if **Use All Reservation Availability Types** is not selected, that at least **Partner API** is selected for the desired area. 


    5.  You may also need to check the **Reservation Settings** and the availability plans to see if Reservations are turned off. 


- Navigate to the **Host Portal**

- Go to sites and choose the affected site

- Then select **Customize **and then **Reservations**. 

- Check to make sure that** Are Reservations Accepted** is set to yes.

- Also make sure that **Using Availability Plans** is set to yes. 

- If the Availability plan flag is set to "No", it is the equivalent to having no availability for both Partner integrations and the Browser Widget. Only the Host clients and those using the PUT Reservations API call (like Disney) will accept reservations with this flag off 


3. If reservations are only not showing availability for one or a few specific days, then it is possible that that Online Bookings have been stopped. 


- Navigate to the **Host Portal**

- Go to sites and choose the affected site

- Then go to operations and then **Reservation Book**. 

- Choose the Calendar date that the caller is reporting and then Look to see If the **Stop Online Bookings** button, is now labeled **Resume Online Bookings**


****