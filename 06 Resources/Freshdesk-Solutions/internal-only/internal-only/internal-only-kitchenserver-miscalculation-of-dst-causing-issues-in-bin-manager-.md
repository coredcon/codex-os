---
title: "*|Internal Only| - KitchenServer miscalculation of DST causing issues in Bin Manager (CSK 5 and CSK 6)"
freshdesk_id: 17000062423
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2017-11-07
updated: 2022-11-01
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000062423
---

# *|Internal Only| - KitchenServer miscalculation of DST causing issues in Bin Manager (CSK 5 and CSK 6)

The following is a known bug in CSK 5 (fixed in version 5.6.117) and CSK 6 (fixed in version 6.1.123).


I wanted to share some information regarding a DST issue I encountered on Sunday. A customer called reporting Bins were not counting. The cause was due to DST being enabled in Windows Time on the Server. In CSK 6.0 until version 6.1.123 there is a bug that miscalculates when to start DST which throws off the time in Bin Manager when converting the local time of the Bin period to UTC for comparison against the kitchen data (CourseStartTime, etc.).


This defect was addressed in version 6.1.123:

## Build 6.1.123.0 – November 8, 2016 (master)


**Number**


**Summary**


**Component**


**Type**
28708
(Support: 001-00-068426) KitchenServer is calculating DST incorrectly causing issues in bin manager
Kitchen Server
Defect


The best solution is to have the customer upgrade to, at least, 6.1.123. However, you can also disable DST on the Server PC and then properly set the time. If you choose this option remember the time will need to be changed every time there is a time change. Also, be sure CP is set to manage time for the controllers (only this option in CP, leave the DST option in CP deselected). If let unchanged, the issue will resolve itself the following Sunday (1 week from the date of the DST change).


Please keep this in mind if you encounter this issue during the first week of a time change.