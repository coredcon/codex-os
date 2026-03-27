---
title: "*|Connect Applications| - Online Ordering and MicrosTSConnect"
freshdesk_id: 17000078539
category: "Support"
folder: "Connect Applications"
status: published
created: 2018-09-19
updated: 2022-07-06
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000078539
---

# *|Connect Applications| - Online Ordering and MicrosTSConnect

Online Ordering and  MicrosTSConnect


** **


**Background:**** **


The QSR Automations  MicrosTSConnect product utilizes the System Interface Module (SIM) made  available by Micros for integrating third-party systems with the Micros RES  3700 POS system.QSR Automations  provides a SIM script file, written in the Micros proprietary Interface Script  Language (ISL), which resides on each POS terminal.The SIM script works in conjunction with a  QsrMicrosTSConnect DLL to send orders from the POS terminal to the QSR kitchen  display system. 


Since this interface  relies on the SIM script and DLL on the POS terminal, online orders injected  into the Micros system via the Micros POS Web API on the Micros server are not  fired to QSR.In order to trigger the  SIM event needed to automatically fire online orders, QSR utilizes a “check trailer”  configured in Micros.This allows the  DLL to send online orders from the Micros server to the QSR kitchen display  system. 


This document outlines  the requirements and configuration steps in the Micros RES 3700 configurator  for setting up online ordering with MicrosTSConnect. 


** **


**Requirements:**** **


• MicrosTSConnect  version 2.0.28.0 or higher (both DLL and EXE) 


• Ops.exe  running on Micros server (see page 4 of this document for more information) 


• SIM script  – the required version of the ISL file will vary depending on the  MicrosTSConnect configuration: 


 


o If configured for “standard” mode… 


 


                    … use the ISL file customized for Online Ordering* 


o If configured for On The Fly mode... 


 


… use the  ISL file customized for On The Fly and Online Ordering*****


 


_*If unsure of the ISL file you need, please contact your QSR  Automations representative. _


 


 


**Micros POS Configurator:**** **


• **Sales** |** Descriptors **|** Trailers **


**    **o Add "QSR Trailer" 


                 


                    Trailer Line 1 = @@QSR_TRLR 


• **Devices **|** Order Devices     **


**        **o Add "ONLINE EXPO"*


§ Header and  Add to Order Header settings may be assigned or left blank per customer  configuration § Trailer - **QSR Trailer**


§ Assign  Device, Backup Device (as needed per customer configuration, but typically a  “Journal”                 printer) § Redirection  Device - **ONLINE EXPO**


§ Check Info Print Format - **After Header**


_*When adding the ONLINE EXPO order device, select a device  number between 1 and 16 to avoid interference with Print Class values sent to  QSR. Using slots 17-32 may cause issues  with routing in the kitchen display system. _


• **Devices** |** Devices **


**        **o Confirm a  Device has been configured as Device Type = PosAPI Web Service o Confirm Network Node selected is                 the POS server machine o If not, create the Device: 


§ Name –  Something with “API” (e.g. WEB API DEVICE) or “TransactionalSvc” for easy  identification § Device Type  – **PosAPI Web Service**


§ Network  Node – use the POS server Workstation node configured at Devices | Network Node  


• **Devices** |** User Workstations **


**        **o On the General tab, confirm the API device is present and  configured per the customer (e.g.,  Revenue Center and                     Default Order Type values are defined) 


 


 


 


 


 


 


 


On the Options tab, enable BOTH of  these options*: 


        § Order  device printing at POS only             


        § Guest Check printing at POS only 


 


_*These “POS only” options allow online orders to fire from any  available Workstation at the time the online order is injected into Micros via  the Pos Web API. If there are no  available Workstations, the online order will be held in Micros until a  Workstation becomes available, then fire to MicrosTSConnect from that  Workstation. _


 


_The customer may choose to only enable the “Order Device”  setting. However, selecting both options  should ensure online orders fire since QSR may not always know the implications  of these settings on the customer’s wider Micros configuration. _


_ _


_By running an instance of Ops.exe on the Micros Server to serve  as a dedicated online order terminal, the customer should always have an  available Workstation for firing online orders as they are received. Otherwise, please note there may be delays  during busy periods where all Micros Workstations are in use and unavailable  for online orders. _


_ _


_ _


_ _


_ _


_ _


_ _


_ _


_ _


 


On the Order Devices tab, for the  API device, select "ONLINE EXPO" under Enable Order Devices 


        § Note: This is  in addition to the existing “Enable Order Devices” settings. 


• **Sales** | **Print Classes **


**        **o Select "Print to... ONLINE EXPO" under Remote  Devices for all existing Print Classes 


            § Note: This is in addition to the existing “Print  to…” settings. 


 


 


 


 


 


 


 


Add new Print Class "ONLINE  ONLY" with "Print to... ONLINE EXPO" selected under Remote  Devices 


    § Print On  options: Customer receipt, Journal, Report, Check 


                            • **Sales **| **Tender Media **o Add "Online Order" with these settings: 


            § General tab: 


                            • Type:Service Total


                        • Print  Class: ONLINE ONLY 


 


 


 


            Menu Level Class: All  Levels 


 


 


 


 


 


§ Service TLL tab: 


 


        Fire Order enabled