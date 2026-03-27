---
title: "*|Internal Only| - Setting up Perfmon to monitor Server performance"
freshdesk_id: 17000069244
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2018-03-22
updated: 2023-09-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069244
---

# *|Internal Only| - Setting up Perfmon to monitor Server performance

# **What is Perfmon?**


Microsoft Performance Monitor, or Perfmon, is used to monitor a computer's performance using counters and trace data so that it might be monitored in real time, or saved to be reviewed at a later date. Below are the instructions for setting Perfmon up to monitor the impact QSR Software is having on a system.


To open Perfmon, simply type Perfom into the Windows search bar


# **Setting up Perfmon**


PerfMon Setup


- Click the start button

- Type PerfMon in the _Search programs and files _box.

- Select perfmon.exe.


- On the left hand side click the arrow next to the “Data Collector Sets” to expand the selection.

- Right click on the “User Defined” option and select “New > Data Collector Set”

- Enter a name into the “Name:” field

- Select “Create manually (Advanced)

- Click “Next”

- Put a check next to the “Performance counter”.

- Click “Next”

- Click “Add…”

- Click the down arrow next to **Memory**

- Select **% Committed Bytes In Use**

- Click Add>>


- Click the down arrow next to **Process**

- Select **% Processor Time**

- In the “Instances of selected object:” select the QSR apps

- **Control Point Client**

- **Control Point Server**

- **KitchenServer**


- Click Add>>


- Select **Handle Count**

- In the “Instances of selected object:” select the QSR apps

- **Control Point Client**

- **Control Point Server**

- **KitchenServer**


- Click Add>>


- Select **Private Bytes**

- In the “Instances of selected object:” select the QSR apps

- **Control Point Client**

- **Control Point Server**

- **KitchenServer**


- Click Add>>


- Click the down arrow next to **Processor**

- Select **% Processor Time**

- In the “Instances of selected object:” select

- **<All instances>**


- Click Add>>


- Click OK

- Click Finish


- On the left hand side of the screen click on the Arrow to expand the selection:

- Data Collector Sets

- User Defined


- Click on the Data Set you just created

- On the right hand side of the screen right click on the “DataCollectorSet01”

- Select Properties

- Set the Log format: to Comma Separated

- Click “OK” and then “Apply”


- In the Toolbar at the top of the screen Click the Green arrow button to start the collection.