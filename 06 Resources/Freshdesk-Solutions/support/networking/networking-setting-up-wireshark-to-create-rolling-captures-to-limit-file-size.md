---
title: "|Networking| - Setting Up Wireshark To Create Rolling Captures To Limit File Size"
freshdesk_id: 17000134275
category: "Support"
folder: "Networking"
status: published
created: 2023-06-09
updated: 2023-10-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000134275
---

# |Networking| - Setting Up Wireshark To Create Rolling Captures To Limit File Size

**Wireshark instructions for a rolling log file**


- Create a folder wherever you want the captures to save and name it something obvious. (EX: Wireshark Logs)

- Run Wireshark As Administrator

- On the top bar choose Capture

- Select Options


- Go to the Output tab

- Check the flag for "Create a new file automatically"


- Check the box for after and set it to 10 minutes


- At the bottom of the from check the box for "Use ring buffer" and set the number of files to keep (Default is 2).


- Choose Browse and navigate to the folder that you created earlier and provide a name for the files to use.


- Click Start to begin capturing data.


***NOTES**: 


- You will need to be ready to stop the capture as soon as the data you are looking for has ben captured as it will only be retained within the timeframe of the files that are saved.

- Make sure to save the open capture when you stop Wireshark as the active data has not been saved to a file yet.