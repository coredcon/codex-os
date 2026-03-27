---
title: "Report Data Formulas (draft)"
freshdesk_id: 17000138726
category: "Support"
folder: "In Progress"
status: draft
created: 2024-01-31
updated: 2024-01-31
views: 0
tags: ["reporting", "Report Viewer", "Insights"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000138726
---

# Report Data Formulas (draft)

Would like to add all reporting data formulas into one article.  Updates to come. 


Rush Item Efficiency:
**Definition:**
(total items – rush items) / total items
Ideal State:
100%
Problem State:
Below 100% indicates that many item prep times are beyond the pre-configured threshold for "Rush" status.  Signals to user an increased risk of quality issues and that they may be accepting too many orders.

Rush Order Efficiency:
**Definition:**
(total orders – rush orders) / total orders
Ideal State:
100%
Problem State:
Below 100% indicates that many order prep times are beyond the pre-configured threshold for "Rush" status.  Signals to user an increased risk of quality issues and that they may be accepting too many orders.

Priority Item Efficiency:
**Definition:**
(total items – priority items) / total items
Ideal State:
100%
Problem State:
Below 100% indicates that many item prep times are beyond the pre-configured threshold for "priority" status.  Signals to user an increased risk of quality issues and that they may be accepting too many orders.

Priority Order Efficiency:
**Definition:**
(total orders – priority orders) / total orders
Ideal State:
100%
Problem State:
Below 100% indicates that many order prep times are beyond the pre-configured threshold for "priority" status.  Signals to user an increased risk of quality issues and that they may be accepting too many orders.

Item Prep Time Efficiency:
**Definition:**
(Total Items Prepped - Items Over Config Prep Time) / Total Items
Ideal State:
100%
Problem State:
Under 100% indicates the % of items with prep time over the configured prep time.  This is a signal to the user that there is a bottleneck forming in prep and that BOH resources need to be reevaluated or the capacity of orders should be reduced.

Item Cook Time Efficiency:
**Definition:**
(Total Items marked “Cooked” - Total Items Over Config Cook Time) / Total Items marked “Cooked”
Ideal State:
100%
Problem State:
Under 100% indicates the % of items with cook time over the configured cook time.  This is a signal to the user that there is a bottleneck forming in prep and that BOH resources need to be reevaluated or the capacity of orders should be reduced.