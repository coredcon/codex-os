---
title: "|Internal Only| - Setting up Event Viewer Auditing for a folder"
freshdesk_id: 17000147636
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2025-08-08
updated: 2025-08-08
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000147636
---

# |Internal Only| - Setting up Event Viewer Auditing for a folder

In **Windows 10** and **Windows 11**, you can configure a folder to log changes—such as modifications or deletions—by enabling auditing through the **Security** section in **Event Viewer**. This is particularly useful when troubleshooting issues involving unexpected file or folder changes, as it provides **timestamped logs** and potential context around the event.

### Benefits of Folder Auditing


- 

Tracks who accessed, modified, or deleted a folder


- 

Provides precise timestamps for changes


- 

Helps identify possible causes of folder disappearance or unauthorized edits


## Step-by-Step: Enable Folder Auditing


- 

**Right-click the folder** you want to monitor and select **Properties**.


- 

Go to the **Security** tab and click **Advanced**.


- 

In the Advanced Security Settings window, select the **Auditing** tab.


- 

Click **Continue** (you may need administrator privileges).


- 

Click **Add** to create a new auditing entry.


- 

Select **"Select a principal"** and type **Everyone**, then click **OK**.


- 

Under **Type**, select **All**.


- 

Under **Basic permissions**, check **Full control**.


- 

Click **OK** to save the changes, then apply and close all windows.


## Viewing Audit Logs in Event Viewer


Once auditing is enabled, Windows will begin logging changes to the folder in the **Security** log of **Event Viewer**.


- 

The key **Event ID** to look for is: **4907**


- 

This event indicates when permissions were modified or when the folder was deleted


- 

To view logs:


- 

Open **Event Viewer** (`eventvwr.msc`)


- 

Navigate to **Windows Logs > Security**


- 

Look for entries with **Event ID 4907**


 

## Important Notes


- 

**Administrator permissions** are required to set up auditing.


- 

Folder auditing may **not work** if:


- 

The user lacks sufficient privileges


- 

Group Policy settings prevent audit logs


- 

The NTFS permissions or system policies block auditing entries