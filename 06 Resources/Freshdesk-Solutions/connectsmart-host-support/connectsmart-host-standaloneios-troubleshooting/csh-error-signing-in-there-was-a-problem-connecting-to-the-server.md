---
title: "*|CSH| - Error Signing In: There was a problem connecting to the Server"
freshdesk_id: 17000061731
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host (Standalone/IOS) - Troubleshooting"
status: published
created: 2017-10-24
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000061731
---

# *|CSH| - Error Signing In: There was a problem connecting to the Server

**Issue: **DineTime Standalone/IOS (Cloud) user attempts to sign in to the DineTime Host application, but receives the following error:


"Error Signing In: There was a problem connecting to the Server"


Troubleshooting:


- **Is the customer trying to use DineTime Host with the DineTime Server application?** 
If No: Proceed to next bullet.
If Yes: Follow these steps below to turn on Server mode:

- Open Settings app on iPad.

- Scroll down to the settings for DineTime Host on the left.

- Toggle the "Use Local DineTime Server" switch on (green).

- Enter the Server IP

- Relaunch DineTime Host App


                


- Have the user open a browser and attempt to use the internet on the iPad to verify internet connectivity.
Obviously DineTime Host requires an internet connection to function.


- If iPad has an internet connection, have the user navigate to [https://portal.dinetime.qsr.cloud]and attempt to log in.  They will receive one of the following messages:

- **"Error: Invalid Password"** - Have the user click "Forgot my Password" and follow reset steps, then attempt login again.

- **"Verification Needed - We need to verify your email address before you can login" **- Have the user click "Send Verification Email Again", then check the email address they are attempting to login with.  They should receive an email with a verification link.  Once they have clicked the link to verify the account, have them attempt to login to the DineTime Host app again.  See ["Verification Needed"] article for further information.