---
title: "* |CSK| - How to set Load Balancing to alternate between two stations"
freshdesk_id: 17000130107
category: "Support"
folder: "CSK"
status: published
created: 2022-12-09
updated: 2022-12-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000130107
---

# * |CSK| - How to set Load Balancing to alternate between two stations

## Goal/Desired Behavior:


The client needs items to display to load balance between two stations. This means that two stations receive the same routing scheme but it may be a high volume area and they have two different stations dedicated to prepping these items and need incoming items to share the volume so one station does not get overwhelmed.


## Steps:


- With the dataset open in Kitchen Builder Pro navigate to Builder > Activity Levels > Activity Levels Settings > Load Balancing > Set Mode as Round Robin

- 


- Navigate to the station settings for the second station that you are wanting to load balance with and under the Advanced tab set the Display Group to a different group than the first station you are wanting to load balance between.

- 


- If successful you will see that orders should be round-robin routing to the stations (in this example).

- 


** Note if the client needs to set limits to how many orders/items each display group can get they can enable the Display Group Capacity under the Display Groups setting. Once enabled they can decide how many orders or items they can receive.