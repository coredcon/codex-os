---
title: "* |CSH| - GRDS Dashboard: How is the  'Guests Seated Per Hour' Dinetime metric calculated?"
freshdesk_id: 17000083587
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Troubleshooting"
status: published
created: 2019-01-02
updated: 2022-12-12
views: 0
tags: ["DineTimeServer", "metrics"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000083587
---

# * |CSH| - GRDS Dashboard: How is the  "Guests Seated Per Hour" Dinetime metric calculated?

**Concern**: 


In ConnectSmart Kitchen, how is the GRDS Dashboard Host Metric "Guest Seated Per Hour" calculated?


**Explanation**: 


The "Guests Seated Per Hour" metric is a rolling total of the number of guests seated within the past 60 minutes. That will include all visits that were seated in the past 60 minute time frame, whether they are currently still seated or have been completed. It does not display an average.


**Example**:  if the time is currently 5:31pm, it would show any guest that had a Seated Time back to 4:31pm. As soon as the clock rolls over to 5:32pm, then it will drop from the count any guests seated prior to 4:32pm.


**Note**: there could be a slight lag in when the counts are updated on the Kitchen Display Clients given the processing time needed to get the data from DineTime Server up to our RealTime Metrics Server and down to Kitchen. However, it should be fairly minimal.