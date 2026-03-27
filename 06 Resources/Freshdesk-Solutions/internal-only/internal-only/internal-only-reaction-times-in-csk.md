---
title: "*|Internal Only| - Reaction Times in CSK"
freshdesk_id: 17000078681
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2018-09-21
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000078681
---

# *|Internal Only| - Reaction Times in CSK

# Overview


When using the delay routing setting where the item timing begins when the first item displayed is started/bumped, other items will appear based on the difference in their cook times. However customers have found that in most cases there is a “reaction time” which is the time it takes for the person working a station to see the item and begin the cooking process. Since the timing doesn’t start until the first item begins, this reaction time setting would be added to the cook times of all subsequent items down the line to better coordinate items completing at the same time.


Functionality


The value of the new setting will be added to the cook times of all items routed to a view that are not the longest cook time item on an order. For example use the classic 10 minute steak, 5 minute burger example and add a reaction time setting of 30 seconds to the grill view. Since the delay timing does not begin until the first item is marked cooking and the steak is the first item displayed, there is no impact/change to the steak’s cook time. However with the reaction time set to 30 seconds for the grill view it is expected to take 30 seconds to see and react to/begin the cooking process for the burger. Therefore the system will add 30 seconds to the cook time of the burger to make the new time 05:30 (330 seconds) and cause the burger to appear 30 seconds before it would have under the current settings. The reaction time should be added to whatever cook time is being used by the item at that station for the purpose of delay routing. In other words, if it is using an alternate cook time (Cook Time 2, 3, 4), if the cook time is modified by a Prep Modifier (Rare, Well Done, etc.) , if the cook time of the side item is used based on other settings on the view template, or if the item is configured to use the plate time and adjust the delay time based on the plate time, in all of those cases the reaction time is added to the time used by the system to determine when to display the item.


The reaction time, when used should only affect the cook time of an item for the purposes of delayed routing only and should not affect any rush or priority times that are based on an offset of or percentage of the individual item’s cook time.


Settings


Since the expected reaction time can vary based on the typical volume levels at a particular station, this setting should be applied at the template level so that users can set a different setting by station if needed. This new setting should only be enabled/available when the user selects the setting for “Calculate Delay From” setting to “Cooking Start Time”


Alternately or in addition to, the kitchen server could calculate a reaction time, we could allow this setting to be configured to be a moving average based on the average real reaction times calculated over the last X minutes and updated at the top of each minute. The challenge with this option would be that not every user uses the “Cook” function to signal that they have started an item, some just simply bump items when completed. This would obviously be the more intelligent and versatile solution but would require additional discussion with development to define the calculation of the “reaction time” and whether or not additional settings were required.


Use Cases
The following use cases would apply if using a “static” reaction time defined by the user.


Example 1 - Static
Customer has 3 line item stations defined in their configuration, Grill, Fry, Salad. Each uses a unique Item View Template. After analyzing speed of service data the customer determines that on average it takes 20 seconds to react to new items on the Salad station, 30 seconds on the Fry station and 45 seconds on the Grill station. Therefore the user configures the reaction time for each station accordingly. Based on those settings the following order is placed:


Item Station Displayed On System Cook Time Cook Time with reaction time added
Steak Well Done Grill 750 seconds (600 second normal time * 125% for Prep Modifier of Well Done 750 (no time added as this item is the longest)
Grilled Chkn Salad Grill 360 seconds 405 (360 + 45 second grill reaction time)
Grilled Chkn Salad Salad 120 seconds 140 (120 + 20 second salad reaction time)


Based on the above the Steak would appear first at the grill station. 345 seconds later (750-405) the Grill Chkn Salad would appear at the grill station then 265 seconds later the Grilled Chkn Salad would appear at the salad station.


Use Cases
The following use case would apply if using a “dynamic” reaction time defined by the user.


Example 1 - Dynamic
Customer has 3 line item stations defined in their configuration, Grill, Fry, Salad. Each uses the same line Item View Template. The template is set to use a system reaction time over the last 15 minutes. At 7:30pm the system has calculated the following average reaction times at each station between 7:15pm-7:30pm. Grill = 53 seconds, Fry = 32 seconds and Salad = 10 seconds. Based on those settings the following order is placed:


Item Station Displayed On System Cook Time Cook Time with reaction time added
Steak Well Done Grill 750 seconds (600 second normal time * 125% for Prep Modifier of Well Done 750 (no time added as this item is the longest)
Grilled Chkn Salad Grill 360 seconds 413 (360 + 53 second grill reaction time)
Grilled Chkn Salad Salad 120 seconds 130 (120 + 10 second salad reaction time)


Based on the above the Steak would appear first at the grill station. 337 seconds later (750-413) the Grill Chkn Salad would appear at the grill station then 283 seconds later the Grilled Chkn Salad would appear at the salad station.