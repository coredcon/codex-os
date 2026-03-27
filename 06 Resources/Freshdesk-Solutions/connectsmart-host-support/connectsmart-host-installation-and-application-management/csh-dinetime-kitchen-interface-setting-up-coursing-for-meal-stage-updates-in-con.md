---
title: "*|CSH| - DineTime Kitchen Interface - Setting Up Coursing for Meal Stage Updates in ConnectSmart Host"
freshdesk_id: 17000061110
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host - Installation and Application Management"
status: published
created: 2017-10-09
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000061110
---

# *|CSH| - DineTime Kitchen Interface - Setting Up Coursing for Meal Stage Updates in ConnectSmart Host

**DineTime Kitchen Interface Builder Settings**


Go to the Kitchen Interface Settings Tab >


Select a Coursing Method from the drop-down menu. 


            **None:** No Items will be coursed.


**Coursing Manager:** Uses Coursing Manager and Routing Categories configured in the DTKI. 


**Course Name:** Assigns items to courses based on the course name associated with the item. (Course Name overrides any configured settings in the Coursing Manager.)


Click **OK** to save settings. 


If the Coursing Manager was selected, go to the **Coursing Manager**. 


Choose the option that matches how the POS sends Kitchen messages. (Total, Tender, or Total or Tender)


Go to the **Coursing Schemes** tab. 


Define here whether the different options will be sent as a separate course and how the courses will be identified. 


Remember Indicator text needs to be defined to match exactly what is sent from the POS. 


                If Coursing by Routing Categories then the Categories will need to be defined in the             **Routing Categories** Section. 


 


**Portal settings**


 


Go to the **Host Portal** > **Sites** > **Customize** > **Interfaces**


Select **Set meal stage when a course is received from the POS** from the Current Meal Stage drop-down menu for the Meal Stage to progress on POS messages. 


Select **Set meal stage when a course prepared event occurs** to progress the meal stage based on an action taken in Kitchen. (This will only work if the customer is a Kitchen subscriber and bumps a course off all prep screens. 


 


You can also define what action ConnectSmart Host will take when a check is Paid/ Closed from the POS.  


            


Once all the settings are configured. Make sure that the DineTime Kitchen Interface is running along with the ConnectSmart Host server.