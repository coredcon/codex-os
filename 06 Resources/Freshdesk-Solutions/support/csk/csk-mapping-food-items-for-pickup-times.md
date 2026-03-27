---
title: "*|CSK| - Mapping Food Items For Pickup Times"
freshdesk_id: 17000137611
category: "Support"
folder: "CSK"
status: published
created: 2023-11-10
updated: 2023-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000137611
---

# *|CSK| - Mapping Food Items For Pickup Times

In some situations, a customer may need to use an item to trigger the Future Order Delay.


For this to function, several things need to be in place:


- The **Destination **must have the option to "**Apply Future Order Delay**" enabled for the destination used for the order.


-  Under **Transaction Manager** - **Field Mappings**, “**Map Pickup Time fields**” must be enabled. 
Additionally, there are two dropdowns to define which format the Date / Time Item should be in:


- Clock Type:

- **AMPM** - Item must include AM or PM (ex. 1:00 PM is sent as 1:00 PM).

- **HR24** - Item sent must be in 24 hour format (ex. 1:00 PM should be sent as 13:00)


- Date Format:

- **Default** - Kitchen will use the default based on the host operating system’s Clock settings.

- **DDMM** - Date should be in DD/MM format (ex: Dec 13 is 13/12)

- **MMDD** - Date should be in MM/DD format (ex: Dec 13 is 12/13)

**Note:** Pickup Times sent without a date should be treated as “same day” orders. Pickup Times sent without a year will be treated as the current year.


3.  Promise Time data should be sent as food items that have either a preceding item or an in-line label that use any of the phrasings below:


- Pickup Time

- PickupTime

- Pick up Time

- Promise Time

- PromiseTime

- Pickup

- Pick up

- Promise

- Time

- PT

- Fulfillment Time

- FulfillmentTime

- Fulfillment

- FT


The method we recommend is using the inline prefix, since sending two separate Items can still result in possible timing issues.


**Examples of working Pickup Time items:**


"Pickup Time 11/08 4:00 PM"


"PT  11/08 4:00 PM"