---
title: "*|CSH| - How to Set up Coursing in the DineTime Kitchen Interface"
freshdesk_id: 17000129733
category: "ConnectSmart Host Support"
folder: "DineTime Kitchen Interface"
status: published
created: 2022-11-21
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000129733
---

# *|CSH| - How to Set up Coursing in the DineTime Kitchen Interface

We have ConnectSmart Host customers who choose to not use our ConnectSmart Kitchen suite of products but still would like to receive Meal Stage Updates for their tables in DineTime as if they were using CSK. This functionality would require the site to have the DineTime Kitchen Interface installed so that it can send meal stages along with other usual information to ConnectSmart Host. 


Once you have the DineTime Kitchen Interface installed on the server you will want to open the DineTime Kitchen Interface Builder via the Start Menu.


You will then want to open the dataset that the site has been using (if this is the first time you will want to choose the option at the bottom to create a dataset).


Click on "Coursing Manager" and a new window will appear you will want to change the "Initiate coursing on:" to TotalOrTender (see screenshot):


Next click on the "Coursing Schemes" tab and then go through each tab and set up "Indicator text:" which is should match verbatim the item that is being sent with the courses (ex. *As App* or *As Entree*). For the Drinks, Appetizers, Soup/Salad, and Desserts course you may have to check the "Send items as a separate course" if you are wishing to utilize those courses. Also for the Drinks, Appetizers, Soup/Salad, and Desserts tabs you can set select a Routing Category that is specific to those courses (if you want to utilize this option you will have to build the categories using "Routing Categories" in the DineTime Kitchen Interface Builder). See screenshot:


Once you have all these changes saved you will want to click Tools at the top of the DineTime Kitchen Interface Builder window and select "Copy Current to Run Time..." and then click OK on the next prompt that appears and then restart the QSR DineTime Kitchen Interface service and DineTime Server service. 


You should now be able to see meal stages when you look at your seated tables in ConnectSmart Host according to which course they are on (see screenshot):