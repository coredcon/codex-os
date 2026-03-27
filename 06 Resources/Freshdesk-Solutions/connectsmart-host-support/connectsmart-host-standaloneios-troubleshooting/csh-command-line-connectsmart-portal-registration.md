---
title: "*|CSH| - Command Line ConnectSmart Portal Registration"
freshdesk_id: 17000132034
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host (Standalone/IOS) - Troubleshooting"
status: published
created: 2023-03-15
updated: 2023-03-15
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000132034
---

# *|CSH| - Command Line ConnectSmart Portal Registration

Instructions for this process can be found in the installation guides.


ConnectSmartRegistration.exe has the ability to run from the command line and perform product registration. 


To register using the Command Line, complete the following steps:


1. Navigate to QSR Enterprise Portal and log in to your account.


2. Navigate to: Company > Site- desired site > Manage > Server Registration.


3. Select Generate Kitchen Code.


4. Select either Primary Server or Secondary Server.


5. Select Generate.


6. A new line entry will appear for ConnectSmart Kitchen Server providing the Enterprise Registration Code and the date it was generated. Copy this code.


7. Run ConnectSmartRegistration.exe with the command line options to make it perform registration:


- Open Command Prompt as Admin

- Navigate to the file path that contains the exe with the following command: "**cd C:\Program Files (x86)\QSR Automations\ConnectSmart\Common\Bin**" 

- **ConnectSmartRegistration.exe <registration code> <product>**

- For example: ConnectSmartRegistration.exe UL5LW1U7 Kitchen

 


8. Refresh the page in Portal and confirm there is a date time stamp listed in the Registered column to ensure registration is completed.