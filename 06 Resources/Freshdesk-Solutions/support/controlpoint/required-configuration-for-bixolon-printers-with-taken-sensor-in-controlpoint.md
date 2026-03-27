---
title: "Required Configuration for Bixolon Printers with Taken Sensor in ControlPoint"
freshdesk_id: 17000148870
category: "Support"
folder: "ControlPoint"
status: published
created: 2025-10-23
updated: 2025-10-23
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000148870
---

# Required Configuration for Bixolon Printers with Taken Sensor in ControlPoint

## 


To ensure Bixolon printers with the Taken Sensor enabled remain reliably online and maintain stable connectivity within ControlPoint, specific minimum software and firmware requirements, as well as configuration settings, must be met.


---


### Minimum Software and Configuration Requirements


Your site must meet the following minimum requirements:


- 

ControlPoint Version: The site must be running ControlPoint 2025.4.13 or higher. 


- 

Printer Template Setting: Within the ControlPoint Printer Template used for the Bixolon device, the Bixolon Command Language must be selected. This ensures that ControlPoint communicates with the printer using the correct proprietary command set necessary for proper operation, including sensor status.


---


### Minimum Firmware Requirement ⚙️


The Bixolon printers themselves must be running a minimum firmware version of v02.07. Printers with firmware older than this version may lack the necessary features or stability required to integrate reliably with ControlPoint's management of the Taken Sensor.


---


If a site does not meet these minimum requirements and configuration settings, the Bixolon printers will experience connectivity issues:


- 

Printers will not stay online in ControlPoint.


- 

The printers may show frequent drops in connectivity, appearing to go offline and then coming back online repeatedly.


Action Required: Ensure your ControlPoint application is updated to the required version, the Bixolon Command Language is selected in the relevant printer templates, and all Bixolon printers are running firmware v02.07 or newer to resolve stability issues related to the Taken Sensor feature.