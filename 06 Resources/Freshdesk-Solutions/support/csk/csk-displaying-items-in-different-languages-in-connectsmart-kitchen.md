---
title: "*|CSK| - Displaying items in different languages in ConnectSmart Kitchen"
freshdesk_id: 17000130081
category: "Support"
folder: "CSK"
status: published
created: 2022-12-08
updated: 2022-12-08
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000130081
---

# *|CSK| - Displaying items in different languages in ConnectSmart Kitchen

## **Goal/Desired Behavior:**


The customer would like to display food items that are being sent from the POS in a different language.


## **Setup:**


- You will need to ensure that the font file for whichever language is being sent by the POS is installed on the ConnectSmart Kitchen server.

- If the Font is not present on the CSK server, you will need to download the correct font file. 

-  Next, open the Kitchen Builder Pro and then navigate to GRDS Color Schemes. 

-  From here you should be able to select the font to use for whichever item attribute in GRDS Color Schemes (i.e. SimSun is a standard Chinese Font) for the items type the POS is sending.


_**NOTE**: CSK is not translating items to the language this is just so that CSK can display the items in the same language they are being sent to us in._


_**NOTE**: There is currently (as of 04/29/2021) not an efficient way to achieve this in Kitchen Enterprise via the Kitchen Portal Builder._