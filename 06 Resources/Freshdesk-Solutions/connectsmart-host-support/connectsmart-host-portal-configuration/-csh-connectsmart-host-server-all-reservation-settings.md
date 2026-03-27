---
title: "* |CSH| - ConnectSmart Host Server - All Reservation Settings"
freshdesk_id: 17000071957
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host Portal / Configuration"
status: published
created: 2018-05-09
updated: 2023-11-08
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000071957
---

# * |CSH| - ConnectSmart Host Server - All Reservation Settings

**Configuring Sessions, Operating Hours, and Exceptions**


Reservation availability settings are customized in the Enterprise Portal. This provides restaurants the ability to limit day parts, days of the week or calendar dates that are open to reservations. 


The initial settings are done at the “Company” level for each site within the Portal as they may affect more than just Reservations. 


-  Log into the Enterprise Portal at: [https://portal.qsr.cloud] 

-  Select the site from the list 

-  Select Operating Hours from the Left Manu Pane 

-  Uncheck unnecessary sessions and name them as desired 

-  Click Save

-  Scroll down the page to reveal Session Hours

- By the day of the week, use the drop-down to show Open and add operating hours for each session

- Click Save 

-  Scroll down the page to reveal Exceptions 

-  Select the Add button 

- Name the event and select whether it’s a One Time thing or recurring, i.e. national holiday 

- Select the date from the calendar 

- Select whether the session is open or closed or if closed the entire day 

- Select done and Save at the top of the page


**Note**: Exceptions will take precedence by third parties, browser widget, in-house, and any API that allows for the creation of reservations.


** Configuring Availability Plans **


Reservation availability is a combination of the Session and Seating Area. Calculating availability is key to not overbooking the restaurant. Decide in advance how many seats will be available for reservations. Reservation Calculation Information DineTime allows restaurants to create multiple plans if necessary. There is one Default plan available which may be changed as needed. Any new plans will take precedence over the default. This includes days of the week or calendar dates. 


In the Enterprise Portal navigate to DineTime from the selector. 


Select the site from the list and navigate to Manage then select Availability Plans. 


Notice there is a Default plan available. This may be customized by selecting the Pencil icon and editing the settings. 


To create a new plan for a given day of the week or date, select the Add icon. Name the plan something that is easy to understand such as a day of the week, a holiday, or another event that impacts business in the restaurant.


After naming the plan select the pencil icon to edit the plan that was just created.


**Note**: The seating areas are created as Seating Areas in Floor Plans and Sessions are configured and described above in this guide.  


This example currently has no reservation availability for any session in any area of the restaurant. Use the drop-down menus to customize the plan 


**Creating Availability **


Choose a calendar date or day of the week that this plan will apply. Availability Play type defaults to Pacing, Slot based is also available. Session Hours by default will use the preconfigured sessions. Customize the times if needed. Booking Intervals are the times that will display in an app or online as the start time for all reservations. The default is 15 minutes, reservation availability will start at the beginning of the session and be offered every 15 minutes to the end of the session. Other options are 30 or 60 minutes. 


**Note**: A custom Reservation table turn can be configured if desired. 


Create in the Customize and Table Settings menu of the Enterprise Portal then they will display as options in Availability. Reservation Availability Type using pacing has 3 options, if using slot based there will be only 1 option.


**Basic Pacing **


Guest counts are used in determining reservation availability. Enter the Maximum total Covers for the Session. In this example, no more than 200 total guests can book a reservation for the Restaurant area during the Breakfast session. Enter a Maximum of Covers per Booking Interval. In this example, no more than 20 guests can book per 15-minute interval (see above for booking interval.)  


**Basic Pacing with Party Size**


 Allows further configuration to the counts by booking interval AND by party sizes of 1-2, 3-4, 5-6, 7- 8, and 9 and over to determine availability. In this example, no more than 200 total guests for the Seating Area of the Restaurant during the Breakfast Session only 20 total guests per 15-minute interval broken down by party sizes to best fit the needs of the restaurant. Twenty total guests could be 1 party of 9 plus a party of 5 plus 3 parties of 2. OR it could be all smaller parties, either way, the total for that interval will never go above 20.


**Interval Filter** 


Customize the exact number of covers (guests) allowed to make reservations for each booking interval, All Party Sizes OR further customize by using the second option of Per Party Size.


 By opting for Per Party Size the ability to ramp up to or scale back large parties or remove large parties from peak hours is possible. In the example below the restaurant has opted for no reservations at all until the 8:00 hour. No more than 10 total covers and all of them would be parties of 2. As the intervals progress, they are able to handle more covers and by 9:30 they will accept 20 covers and accommodate parties of up to 7. 


**Note**: Any availability can be overridden by contacting the restaurant and the appropriate person accessing the Client or Portal to create the reservation. 


**Note**: Remember to click Done after any changes and Save at the top of the page when working in the Enterprise Portal.


 


Slot based availability 


Use Slot based availability to specify the exact number of covers by party size per interval.


**Reservation Settings**


 Beyond Availability Plans there are settings that effect creating Reservations in general. Under Customize and reservations in the Portal. Use the drop downs to make selections. 


General Settings 


- Are reservations accepted Yes or No? 

- Would you like to use the Availability Plans created earlier? Opting to NOT use will default to in-house reservations only. Hosts would override and manually enter all reservations at the host stand or in the Portal.


- Allow Reservation Availability Override is two parts. Party size and day/time. Who is able to do one or both is configured at the User level. 

- Require Phone number Yes or No. 

- Upcoming Reservation Threshold adds the party to the Wait tab under the heading of Upcoming Reservations. 

- Impending Reservation Threshold moves the party to the active wait to become part of the quoting that is given to walk-in parties.  


**Configuring Seating Areas**


 


Reservation Availability is based on a combination of session and seating areas as we saw earlier. Up to six Seating Areas can be configured for your restaurant. 


Floor Plans


 Adding seating areas is common when restaurants have areas of the restaurant that are used for specific purposes or are seasonal. Patios, Bar Areas, or Game Areas may be examples of spaces where guests could seat but may not be available for reservations.


Add seating areas by using the "+"  Floor Plans menu within a site.


- Name the area as this will be assigned to tables within the floor plan itself. 

-  Select a Booking period that will determine how far in the future reservations can be made. 

-  Credit Card Required Yes or No, at this time there is no bearing on the ability to make reservations based on this setting. 

-  Booking Protection Time is the amount of time applied to the current local time that provides a buffer before a reservation can be made. If the restaurant is regularly on a 1-hour wait at dinner maybe set the buffer at 2 or 3 hours (or longer) to prevent reservations from bypassing the waitlist.  

- Maximum Cover Capacity is the total number of seats in this particular seating area. 

- Fill out the Minimum and Maximum party size questions and click Done. Note: The min and max party settings are separated by in-house and online sizes. In-house, these may be overridden if the user logged in has that permission. Note: Repeat these steps for each Seating Area as needed.