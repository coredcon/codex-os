---
title: "* |CSH| - Understanding Quote Calculation methods"
freshdesk_id: 17000083591
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host Portal / Configuration"
status: published
created: 2019-01-02
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000083591
---

# * |CSH| - Understanding Quote Calculation methods

ConnectSmart Host offers (6) different methods for calculating wait times. Each of these options is described in further detail below. A store's quote method is set in the Host Portal >> Sites >> Customize >> Quote Times >> General Settings >> Calculation Method).


**1: Fixed Quote for Party Size**


Provides a fixed (static) quote time depending on the number of guests in a party  (e.g. for a party of 2, the quote will always be the same regardless of how many parties of 2 are ahead). _A fixed quote does not use any historical data or table turns in the system and does not look at current seating or seated tables.  _The value we return is configurable in the table below found in the portal (Customize >> Quote Times >> Fixed Quote per Party Size Selections).


**2****: Table Turns**


Provides a calculated quote based upon current Seated Parties and Waitlisted parties and uses the configured Table Turn Times in the portal to predict the estimated wait.


Table Turn values are found in the portal (Customize >> Table Settings >> Table Turn Times)


Note: A customer can define multiple Table Turn schemes and apply them to different days/sessions. Typically a site will use a single scheme but they can define more than one.


Example: A restaurant has set a 45-minute wait for a party of 4 in portal. Let's assume they only have one 4-top table in their restaurant and it was sat 20 minutes ago.


The quote for the next party of 4 would be 25 minutes (45-minute portal setting - 20 minutes seated party has occupied table = 25 minute wait for a new party of 4).


**3: Historical Wait Times**


Provides a calculated quote using the restaurant’s visit history to estimate wait based on the average wait time for a party of the same size arriving on the same day of the week during the same 15-minute interval over the past X weeks (X being the configured number of weeks used for forecasting in the portal). The number of historical weeks used for forecasting is set in the portal (Customize >> Quote Times >> General Settings >> **Number of Weeks Used for Forecasting).**


Note: _When using historical data, all parties must: be cleared within 6 hours of being created, have a seated time, and not be a reservation party. If a party is not completed, it will not count toward historical seated times._


 


**4: Historical Table Turns**


Provides a calculated quote and is similar to "Table Turns" but rather than using the configured Table Turn Times, it uses the restaurant’s visit history to estimate wait based on the average table turn time of a party of the same size arriving on the same day of the week during the same 15-minute interval over the past X weeks waited (X being the configured number of weeks used for forecasting).


The number of historical weeks used for forecasting is set in the portal (Customize >> Quote Times >> General Settings >> **Number of Weeks Used for Forecasting).**


Note: _When using historical data, all parties must: be cleared within 6 hours of being created, have a seated time, and not be a reservation party. If a party is not completed, it will not count toward historical seated times._


**5: Guest on Wait List**


Provides a fixed (static) quote time depending on the number of parties currently on the wait list  (e.g. if 2 parties are currently on wait, regardless of party size, the quote will always be the same). _A fixed quote does not use any historical data or table turns in the system and does not look at current seating or seated tables.  _The value we return is configurable in the table below found in the portal (Customize >> Quote Times >> "Guests on the Wait List" Selections).


 


**6: Guest Per Hour (GPH)**


A slot-based algorithm based on the number of guests the restaurant can accommodate per hour. Guests Per Hour divides wait times into 5-minute sections. Each 5-minute section (5-minute wait - 10-minute wait - 15-minute wait etc) is defined by a number of "slots (think excel rows)".  The higher the GPH number, the more slots make up a quote segment section as calculated by (GPH value / 30). Portal offers (4) GPH selections with a pre-assigned GPH value and (1) in which the customer can define their own GPH value (GPH Configurable).


Example: Guest Per Hour 150 = (150 / 30) = 5 slots per quote section.


Note: GPH100 is the only GPH selection that uses a hardcoded 3/4/3/4 etc row count rotation per section and does not use (GPH value / 30).


Note: If using the _Use Quote Ranges_ "Presentation Style" instead of _Use Exact Quotes_, the guest quote will be derived from the _QuoteSelections_ table in Portal. Quote Selections can be configured separately for large parties.


-First, determine how many rows a party of a given size occupy s on the chart to see which quote segment they fall into:


For any of the GPH methods, party sizes 6 and under are each depicted as 1 line on the chart. The amount of lines given to parties containing more than 6 guests is determined by an equation.


Take the party size and divide by 4. Round this quotient up and add 1. Example: A party of 7 would take up 3 lines on the table (7÷4=1.75, round to 2+1=3). A party of 12 would take up 4 lines on the table(12÷4=3+1=4).


-Now we know which quote segment the party falls into, we need to determine where we are going to pull the quote:


* Party size of (1 to [[Customize>>Party Settings>>Large Party Size –1]): - uses relevant record in Quote Selections table in Portal to pull quote (Quote range label or Exact range label depending on Presentation Style)


* Party size of ([Customize>>Party Settings>>Large Party Size] to 11): Similar to the method described above, unless the Portal option "Use a separate set of quote selections when the party size is [Customize>>Party Settings>>Large Party Size] or greater ".


* Party size of 12+: Add 15 to the Exact Quote, use the quote table as determined above.


 


**Note:**** **The Guests Per Hour quote calculation method includes all unarrived call-ahead in the system when determining the number of “wait lines” to use when generating a quote.


**Note:**** **If you are using the Guests Per Hour quote method, even if you **Include reservations in the quote time calculations **selected, reservations will not affect the quoted time until the guest is marked arrived.