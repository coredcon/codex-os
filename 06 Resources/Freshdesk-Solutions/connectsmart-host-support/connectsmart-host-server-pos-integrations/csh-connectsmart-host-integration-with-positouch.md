---
title: "*|CSH| - ConnectSmart Host - Integration with POSiTouch"
freshdesk_id: 17000060020
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host Server - POS Integrations"
status: published
created: 2017-09-14
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000060020
---

# *|CSH| - ConnectSmart Host - Integration with POSiTouch

**ConnectSmart Host supports the following integration features with POSiTouch:**


- Automatic seating of unoccupied tables when an order is started in POSiTouch (via CSK 5+ or DineTime Kitchen Interface)

- Update table color to reflect current Meal Stage (via CSK 5+ or DineTime Kitchen Interface)

- View Check Detail in DineTime Host (via CSK 5+ or DineTime Kitchen Interface)

- Open a new check in POSiTouch each time a guest is seated in ConnectSmart Host Server (via DineTime POS Interface)


**Note**: Turning on automatic seating of of unoccupied tables while also running DineTime POS Interface will result in duplicate checks in POSiTouch (check opened in POSi seats party in ConnectSmart Host which triggers open check in Posi).


Messages do not flow directly from PosiTouch to DineTime, but rather from the POS to ConnectSmart Kitchen (or DineTime Kitchen Interface) to DineTime.


**DineTime Kitchen Interface**


If the restaurant is not using CSK 5 or later, the DineTime Kitchen Interface will need to be installed to pass messages from the POS to DineTime.


For installation/setup instructions, see the **DineTime ConnectSmart Kitchen Interface User's Guide** found in the Documentation folder included with the DineTime installer.


**Configuration Options in DineTime Portal**


- **Automatic Seating of Unoccupied Tables**

- Navigate to the site level of **Host ****Portal** -> **Customize** Tab -> **Interfaces**

- Under **Point of Sales** section, check the box for "_Use automatic seating of unoccupied parties when an order is starte__d_"


- **Update table color in DineTime Host to reflect current Meal Stage**

- Navigate to the site level of **Host Portal** -> **Customize** Tab -> **Interfaces**

- Under **Point of Sales **section, set Current Meal Stage to one of the following two settings depending on whether the restaurant would like the color to change when a course is ordered or when it is marked prepared (if using CSK 5 or later).  

- Set the meal stage when a course is received from the POS

- Set the meal stage when a course prepared even occurs


- Under **POS Check Paid **choose what the restaurant would like to happen when the check is marked paid in POSiTouch

- Clear a table when marked as paid on the point of sale terminal

- Dirty a table when marked as paid on the point of sale terminal

- Do nothing when a table is marked as paid on the point of sale


- Navigate to the site level of **Host Portal** -> **Customize** Tab -> **Table Settings**

- Scroll down to **Table Meal Stage Colors**, set the desired table color for each Meal Stage


**DineTime POS Interface**


DineTime POS Interface is a helpful tool that works in conjunction with POSiTouchTSConnect to open a new check in POSiTouch each time a guest is seated in ConnectSmart Host Server. The new check includes the guest’s name, table number, loyalty ID, and allergy info as applicable.


See [Installing / Configuring the DineTime POS Interface] for setup instructions.