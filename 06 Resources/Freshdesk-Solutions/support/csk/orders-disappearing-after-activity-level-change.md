---
title: "Orders Disappearing after activity level change"
freshdesk_id: 17000143270
category: "Support"
folder: "CSK"
status: draft
created: 2024-10-31
updated: 2024-10-31
views: 0
tags: ["Orders disappear", "Activity level change", "Station view IDs"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000143270
---

# Orders Disappearing after activity level change

If a customer reports that orders disappear after an activity level change, review the following to resolve the issue.

**Step 1:**
Once connected to the customer's Primary kitchen server, click on start and find the QSR folder, then open ConnectSmart Kitchen Builder Pro. (Pro Tip: If they use a portal dataset you can pull the Enterprise data folder and that will contain the applied Dataset)


**Step 2:**
** **Open the Dataset currently used at the location and find "View Manager" under View Settings.


**Step 3:**
Confirm that in the "Activity Levels" tab that "Preserve Routing" is selected.


**Step 4: **
Click on "Selected Activity Level", from the drop-down choose and review each activity level to confirm that the stations configured have matching View ID's, for example, Station 1 should have the same view ID in all the configured activity levels.