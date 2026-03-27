---
title: "*|Internal Only| - Using Notepad++ in Support Environment"
freshdesk_id: 17000060809
category: "Internal Only"
folder: "Support Tools"
status: published
created: 2017-10-04
updated: 2024-10-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000060809
---

# *|Internal Only| - Using Notepad++ in Support Environment

[Download Notepad++] (Version 7.5.1)


**Always make sure you are running the latest version of Notepad++**


This Article is split into 2 sections:


- **Why use Notepad++?**

- **Importing User Defined Language file**


**Section 1 – Why use Notepad++?**


Notepad++ is an alternative to Microsoft’s Notepad that targets programmers and scripters. Some of the things that make Notepad++ a must-use program for us are:


- Color coding sections of scripts such as .xml files to make it easier to find information:


        


       2.Enhanced searching that allows you to show all instances of a search result in one or multiple open files all together:


            


        3. Log monitoring - The ability to refresh a log in real time to show log updates without having to close and reopen the file (similar to Linux tail –f)


**Section 2 – Import Custom LOG settings**


I have created a custom User Defined Language file for logs. This will change the colors of certain commonly searched for words and phrases in our logs. Right now this will color code the words/phrases:


- error

- failed

- Terminating

- "shutting down"

- "The socket connection has been reset."

- "Login failed for user 'QsrUser'. "

- "A valid dataset could not be found"

- "Index outside the bounds of array"

- "A valid kitchen server product license could not be found"

- "ConnectSmart Kitchen Server shutting down..."

- It also colors the numbers so they stand out


**Please let me know of any other common msgs you would like to add to this list.**


Examples:


**Attached to this document you will find Log_default.xml. This file needs to be imported into Notepad++ in order to update the language file for .log files.**


**NOTE: This xml assumes you are using the default color scheme. If you would like an customized version to match your custom color scheme, you will need to tweak the xml styles. If you need help with this, let me know.**


- In Notepad++, go to Language>Define your language:


            


        2. In the User Defined Language form, click on Import. Then browse to where you saved the Log_default.xml and click Open.


        3. Close out the User Defined Language form. Then close out Notepad++ and reopen it. Open a new .log file and any of the above keywords should be tagged.


*The Support_Colors file is updated with additional messages that it looks for but is designed to be used with the Vim Dark Blue style in Notepad++

**I have made an alternate version of the same file called DarkModeColors that works with most colors schemes with a darker background. It does not work very well with White though as the primary text color is very light. This is the one you would likely want to use if yo are not using the Vim Dark Blue style in Notepad ++