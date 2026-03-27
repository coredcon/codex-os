---
title: "Troubleshooting Google Reserve and Google Waitlisting"
freshdesk_id: 17000141065
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host Partner Integrations"
status: published
created: 2024-05-16
updated: 2024-05-16
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000141065
---

# Troubleshooting Google Reserve and Google Waitlisting

**Troubleshooting Google Reserve and Google Waitlisting**


 


QSR has two different WebAhead (online waitlisting) and Reservation partner integrations. Customers may call in because they are facing challenges with either getting availability from ConnectSmart Host or the integration working at all. This document will outline the most common issues and how to troubleshoot them.


 


**Google Reserve and Google Waitlisting buttons are Missing**


If a customer calls in and indicates that they should have the Reserve a Table or Join Waitlist buttons on the Google Maps webpage as shown below, then you will need to check a few settings in both the Admin and Host portals. **Please keep in mind, if the customer was only activated for the Google integration the same day, there is a chance that it just hasn't updated on the Google side yet and troubleshooting beyond the first step may not be necessary****. **


- First, you will need to verify that the integration has been enabled for that site.

- Navigate to the **Admin Portal** ([https://admin.qsr.cloud])

- Search for the Site

- From the menu on the left, Expand the** Partner Settings** menu and then go to **Site Partner Settings**.

- Scroll Down to look for **Google Maps Booking** and **Google Waitlist**.

- If these are checked, then the integration is active, and you will need to do further research.

- If these are not checked, then you will need to reach out to the Technical Projects team to get this activated if the location has a supporting subscription. 

- If the subscription does not support the Partner integration, then please contact the account or channel manager teams

- 

- Check Salesforce for what is included in their Subscription


    3. If the integration is enabled and further troubleshooting is needed, you will need to also check the **WebAhead settings**. 


- Navigate to the **Admin portal**.

- Search for the affected site.

- Expand the **Site Settings** menu on the side. 

- Click on **WebAhead Settings**. 

- Please note that the first line under **Visit Source is a dropdown menu**. 

- Verify if the site is using Concept Settings. If so, navigate to the concept level settings that this site is located under. 


- Select **Online Partner Integration** from the drop-down menu and verify. 

- That Web Reserve Status is set to Accepting for Google Reserve

- That WebAhead Status is set to Accepting for Google Waitlisting. 


- If the customer is reporting problems with an option that is set to Not Accepting, please reach out to the Technical Projects team to enable the desired option.   


    4. If this still does not resolve the issue, you will want to check the Host Portal for a few settings. 


- Navigate to the **Host Portal** ([Https://Portal.Host.qsr.cloud]) 

- Go to sites and choose the affected site

-  Then go to **Floor Plans** and then **Seating Areas**

- Scroll down to the Reservation Availability Types and ensure that, if **Use All Reservation Availability Types** is not selected, that at least **Partner API** is selected for the desired area. 


    5.  Lastly, you can check the **Reservation Settings** and the availability plans to see if **Reservations** or **Webaheads** are turned off. 


- Navigate to the **Host Portal**

- Go to sites and choose the affected site

- For **Reservations**

- Go to **Customize **and then **Reservations**

- Check to make sure that** Are Reservations Accepted** is set to yes. 


- For **Webaheads** 

- Go to Manage and then **Availability Plans**. 

- Edit the needed **Availability Plan**

- Scroll down and make sure that **WebAhead Availability** is enabled. 


 


**Google Reserve is Missing Availability**


If A customer calls in reporting that they are not getting any reservation availability in the Google Reserve integration for a specific day or in general, then you will need to check a few different settings. 


1. You will need to check the **WebAhead settings**. 


- Navigate to the **Admin portal**.

- Search for the affected site.

- Expand the **Site Settings** menu on the side. 

- Click on **WebAhead Settings**. 

- Please note that the first line under **Visit Source is a dropdown menu**. 

- Verify if the site is using Concept Settings. If so, navigate to the concept level settings that this site is located under. 


- Select **Online Partner Integration** from the drop-down menu and verify. 

- That Web Reserve Status is set to Accepting for Google Reserve


- If the customer is reporting problems with an option that is set to Not Accepting, please reach out to the Technical Projects team to enable the desired option.  


 2. You may also need to check  the **Reservation Settings** and the availability plans to see if **Reservations** or **Webaheads** are turned off. 


- Navigate to the **Host Portal**

- Go to sites and choose the affected site

- Then select Customize and then Reservations. 

- Check to make sure that** Are Reservations Accepted** is set to yes.

- Also make sure that **Using Availability Plans** is set to yes. 

- If the Availability plan flag is set to "No", it is the equivalent to having no availability for both Partner integrations and the Browser Widget. Only the Host clients and those using the PUT Reservations API  call (like Disney) will accept reservations with this flag off 


3. If reservations are only not showing availability for one or a few specific days, then it is possible that that Online Bookings have been stopped. 


- Navigate to the **Host Portal**

- Go to sites and choose the affected site

- Then go to operations and then **Reservation Book**. 

- Choose the Calendar date that the caller is reporting and then Look to see If the **Stop Online Bookings** button, is now labeled **Resume Online Bookings**


****