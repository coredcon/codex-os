---
title: "*|Hardware| - Jtech IStation FAQ - Darden"
freshdesk_id: 17000078530
category: "Support"
folder: "Hardware"
status: published
created: 2018-09-19
updated: 2022-08-02
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000078530
---

# *|Hardware| - Jtech IStation FAQ - Darden

**How do you check the Firmware on the transmitter?**


To check the firmware on the transmitter, simply power cycle (unplug the power cable and plug it back in) the transmitter. As the transmitter is powering on, the  display will show the firmware and how the transmitter is set up (Fig. A). PVer is the software version. Also displayed is the Baud rate and Base ID of  the system.  


**Note:** Almost all Olive Garden restaurants should Firmware version 2.34  or above. Anything transmitter that is lower than 2.34 should be replaced. If customer is in warranty, they can send the transmitter in for repair.


**Please confirm how any customer would connect this to work with 3rd party software.  What does the software need to communicate to the transmitter?**


Typically, the customer will use the standard db9 serial cable (male to female) to connect to their terminal, which is provided with the ISTATION.  However, as companies are upgrading their POS terminals, we are discovering that these terminals do not have serial ports. Companies generally supply the db9 to RJ45 cable needed to connect our transmitter to DineTime. 


When a technician is installing our paging system with the customer’s POS, the technician needs to follow our RS232 data protocol. Software may have different procedures for initial setup, however they typically use the same setup:


**
**


**RS232 DATA PROTOCOL (Olive Garden / HME)   **   


    - SYSTEM BAUD RATE : 9600       


    - DATA BIT : 8       


    - PARITY BIT : NONE      


     - STOP BIT : 1   


    - PAGER BAUD RATE: 1200    


**RS232 DATA PROTOCOL (Longhorn / JTech)     **


    - SYSTEM BAUD RATE : 1200       


    - DATA BIT : 8      


     - PARITY BIT : NONE       


    - STOP BIT : 1   


    - PAGER BAUD RATE: 512  


Note: All new Longhorn locations will be receiving the ISTATION with HME programmed digital JTech pagers. Please use the RS232 Data Protocol for HME paging.  


**Firmware is up to date, the RS232 settings are correct, and I can manually page the pagers but I cannot page through the POS system. What seems to be the issue?**


If everything seems correct and the technician can manually page the pagers but cannot page through the POS system, have the technician re-seat (unplug the plug in) the DB9 serial cable. Once that is done, power cycle the Transmitter. Note: If the technician or store manager is installing a new or replacement ISTATION, make sure they use the new power supply and DB9 serial cable that is supplied with the transmitter.  


ISTATION FAQs


Fig A


**
**


**I cannot page through the POS system or the transmitter, what is the problem?**


    


If everything is setup up properly and the technician cannot page manually then we need to check the Base ID or Capcode.  


    1. Press the SETUP button on the keypad (Fig. B). The display will show PASSWORD. Type 9731 then press ENTER. 


    2. Press the MENU key (*) repeatedly until you get to the option Set Base ID (Fig. C).  


    3. Press ENTER to change the Base ID then press ENTER again to make sure it is saved. 


    4. Press the CANCEL twice to go back to the home screen. Note: The Base ID of the system matches the capcode setting in the software. Base ID should not be 070.


Fig. B  Fig. C


**Which transmitter is the Technician working with?**