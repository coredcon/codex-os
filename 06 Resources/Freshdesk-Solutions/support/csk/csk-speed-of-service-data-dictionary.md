---
title: "*|CSK| - Speed of Service Data Dictionary"
freshdesk_id: 17000137923
category: "Support"
folder: "CSK"
status: published
created: 2023-11-29
updated: 2023-11-29
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000137923
---

# *|CSK| - Speed of Service Data Dictionary

Speed of Service (SoS) is the functionality involved in tracking and recording various Kitchen events (bumping items/orders, cooking items, etc.) to be able to report on them later.


SoS Event Field
Format
Description**TimeStamp**
DateTime
The time at which the record was generated.
**TransactionNumber**
Integer
The transaction number associated with the record.
**TransactionStartTime**
DateTime
A timestamp of when the transaction was started.
**CourseNumber**
Integer
The course number associated with the record.
**CourseStartTime**
Integer
A timestamp of when the course was started— all other time offsets are based off the Course Start Time.
**CourseName**
Alphanumeric (25)
The name of the course, as defined in the Coursing Manager in Kitchen Builder.
**CourseType**


Alphanumeric (25)
The type of course: Drinks, Appetizer, Soup/Salad, Entree, Dessert, or Bin.
**ItemNumber**
Integer
The unique item index number within the associated transaction.
**ParentItemNumber**
Integer
The item number of the associated parent item within the associated transaction.
**ItemID**
Integer
The item ID or PLU number provided by the POS.
**ItemDescription**


Alphanumeric (25)
The item description provided by the POS.
**ItemQuantity**
Integer
The quantity associated with the record.
**ItemCookTime**
Integer
The item’s programmed Cook Time used by CSK.
**ItemCategory**
Integer
The item category number provided by the POS.
**ItemCookStartTime**
Integer


The number of seconds after the Course Start


Time when an item is marked as cooking.
**Modifier1ID**
Integer
The item ID or PLU number of the first main item modifier.
**Modifier2ID**

IntegerThe item ID or PLU number of the second main item modifier.**Modifier3ID**
Integer
The item ID or PLU number of the third main item modifier.
**ItemTagTime**
Integer


The number of seconds after the Course Start


Time when an item is tagged within an order.
**TerminalNumber**Integer
The terminal number associated with the record.
**Destination**
Integer
The destination ID associated with the record.
**DestinationName**
Alphanumeric (25)
The destination name associated with the record.
**Table**
Alphanumeric (25)
The table number (or name) associated with the transaction.**ServerID**
Integer
The server ID associated with the record.
**ServerName**

Alphanumeric (50)
The server name associated with the record.
**StationType**Alphanumeric (25)
The type of virtual display (Expediter, Prep, Assembler).
**ActivityLevel**
Integer
The current activity level in use.
**DisplayGroupID**
IntegerThe display group the virtual display is part of.
**ViewID**
Integer
The view display ID.
**ViewName**
Alphanumeric (25)
The view display name.
**SOSTag**
Alphanumeric (25)
The Speed of Service tag associated with the record.
**CoursePreparationTime**
Integer
The number of seconds that the course should theoretically take to prepare—also the cook time of the longest item in the course.
**CoursePaidTime**
Integer


The number of seconds after the Course Start


Time when an order is paid.
**CourseParkTime**
Integer
The number of seconds after the Course Start Time when an order is parked.
**FirstDisplayedTime**
Integer
The number of seconds after the Course Start Time when the order/item was first released to a view, but not necessarily visible (e.g. If many orders exist on the view, it may be located in the scroll queue, and therefore, not immediately visible).
**FirstViewedTime**Integer
The number of seconds after the Course Start Time when the order/item was first visibly displayed on a station.
**FirstStoreTime**Integer


The number of seconds after the Course Start


Time when the order is first stored.
**LastRecallTime**
Integer
The number of seconds after the Course Start Time when the order is last recalled.
**LastTotalTime**
Integer


The number of seconds after the Course Start


Time when and order is last totaled.
**FirstTenderTime**
Integer
The number of seconds after the Course Start Time when the order is first tendered.
**LastBumpTime**
Integer


The number of seconds after the Course Start


Time when an order/item is last bumped.
**LastUnbumpTime**
Integer
The number of seconds after the Course Start Time when an order/item is last unbumped.
**LastPreparedTime**
Integer


The number of seconds after the Course Start


Time when the order goes prepared.
**PriorityStatusReached**
Bit (1=true, 0=false)
Boolean which denotes whether an order reached priority status.
**PriorityTime**
Integer


The number of seconds after the Course Start


Time when an order goes into a priority state.
**RushStatusReached**
Bit (1=true, 0=false)
Boolean which denotes whether an order reached rush status.
**RushTime**
Integer


The number of seconds after the Course Start


Time when an order goes into a rush state.
**FoodDelivered**
Bit (1=true, 0=false)
Indicates whether or not food has been delivered when using HME Table Locators.**FoodDeliveredTime**
Integer
The number of seconds after the Course Start Time when food has been delivered when using HME Table Locators.
**TopLevelItem**
Bit (1=true, 0=false)
1 is Parent Item, 0 is Child Item.
**FastTrackedTime**
Integer
The number of seconds after the Course Start Time when an item marked by a keypad action as “Reprioritize Order.”
**RemakeTime**Integer
The number of seconds after the Course Start Time when an item is marked for Remake on an Expo and will be removed from all preps and rerouted.