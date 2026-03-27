---
title: "*|Internal Only| - Course Pacing"
freshdesk_id: 17000069517
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2018-03-29
updated: 2022-11-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069517
---

# *|Internal Only| - Course Pacing

# 


Course longest cook time is used rather than forecast prep time to determine course delay because forecast prep time depends on which views items are routed to, but routing is not performed until the course is released from delay.


The activation time of a course is determined by the previous course’s activation time, longest cook time, _Course delay time_ setting, and the current course’s longest cook time. The previous course’s expected preparation time is calculated by adding its longest cook time to its activation time. Then, the _Course delay time_ for the previous course’s course type is added to the previous course’s expected preparation time to find the expected preparation time of the current course. Finally the, current course’s longest cook time is subtracted from its expected preparation time to find the activation time for the current course.


Course delay is recalculated every second to take into account changes that affect the course longest cook time. Early course preparation (before the course’s longest cook time) can also cause other course delay times to be adjusted. A course’s delay cannot be adjusted once it has been released (it cannot go back into delay). Here are some things that can cause a course cook time adjustment:


- Bin cook time adjustment

- Add-on items

- Voided items

- Voided courses


Course pacing cannot be used with course merging. Each round of courses will be delayed independently from other courses in the same transaction.


## _Examples_

**Course Type**
**Course delay time (seconds)**
Drinks
N/A
Appetizers
40
Soup/Salad
20
Entrees
50
Desserts
N/A


## 1. Entrée released before appetizer


The entrée course is displayed in the kitchen before the appetizer since the entrée’s longest cook time is greater than the appetizer’s longest cook time plus course delay time. The entrée is displayed immediately, and the appetizer is display 60 seconds later.


**Item**
**Course**
**Item Longest Cook Time (seconds)**
Spinach Flatbread
Appetizers
20
JD Stk & Shrimp
Entrées
120


## 2. Entrée released before appetizer, entrée prepared early


This is example would be the same as example 1, but at 30 seconds the entrée course is prepared, which causes the appetizer course to be released immediately after.


**Item**
**Course**
**Item Longest Cook Time (seconds)**
Spinach Flatbread
Appetizers
20
JD Stk & Shrimp
Entrées
120


## 3. Appetizer released before entrée


The appetizer course is displayed first in the kitchen since the entrée longest cook time is less than the appetizer longest cook time plus the appetizer course delay time. The entrée is displayed 30 seconds after the appetizer (20 + 40 – 30 = 30).


**Item**
**Course**
**Item Longest Cook Time (seconds)**
Spinach Flatbread
Appetizers
20
JD Ckn & Shrimp
Entrées
30


## 4. Appetizer released before entrée, appetizer prepared early


This is example would be the same as example 3, but at 10 seconds (10 seconds earlier than the expected prep time) the appetizer course is prepared, which causes the entrée course to be released 10 seconds earlier than originally expected.


**Item**
**Course**
**Item Longest Cook Time (seconds)**
Spinach Flatbread
Appetizers
20
JD Ckn & Shrimp
Entrées
30


## 5. Bin cook time adjustment for appetizer


The entrée course is displayed in the kitchen before the appetizer since the entrée’s longest cook time is greater than the appetizer’s longest cook time plus course delay time. Since the BBQ Ckn Flatbread is a bin item, and the bin is configured with a cook time percentage of 50%, the appetizer course cook time changes from 30 seconds to 15 seconds and the appetizer display 65 seconds after the entrée.


**Item**
**Course**
**Item Longest Cook Time (seconds)**
BBQ Ckn Flatbread
Appetizers
30 (15 with bin cook time adjustment)
JD Stk & Shrimp
Entrées
120


## 6. Add on entrée


The Sizzling Ckn entrée course is displayed in the kitchen before the appetizer since the entrée’s longest cook time is greater than the appetizer’s longest cook time plus course delay time. Before the appetizer is released, a Sizzling Stk item is added on to the entrée course, which increases the entrée course’s longest cook time. The appetizer course activation time is updated so that its expected prep time will be 40 seconds (the appetizer course delay time) before the new expected prep time of the entrée course.


**Item**
**Course**
**Item Longest Cook Time (seconds)**
Spinach Flatbread
Appetizers
20
Sizzling Ckn
Entrées
120
Sizzling Stk
Entrées
130


## 7. Two rounds of courses in the same transaction


The first appetizer and entrée are ordered together, and the transaction is totaled and tendered. The second appetizer and entrée on the same transaction are ordered a few seconds later, and they are delayed separately. In each round, the entrée courses display before the appetizer courses, but they delays are calculated independently.


**Item**
**Course**
**Item Longest Cook Time (seconds)**
Spinach Flatbread
Appetizers
20
Sizzling Ckn
Entrées
120
BBQ Ckn
Appetizers
30 (15 with bin cook time adjustment)
Sizzling Stk
Entrées
130


## 8. All course types in one transaction


This transaction contains a course of each type. The Entrées course displays first. At 20 seconds the Soup/Salad course displays. At 40 seconds the Appetizers course displays. At 55 the Drinks course displays. At 140 seconds the Desserts course displays


**Item**
**Course**
**Item Longest Cook Time (seconds)**
Coke
Drinks
5
Spinach Flatbread
Appetizers
20
French Onion Soup
Soup/Salad
80
JD Stk & Shrimp
Entrées
120
Caramel Cake
Deserts
30