---
title: "*|Validation| CSK 7 SW/Win10 Compatibility Issue"
freshdesk_id: 17000119992
category: "Internal Only"
folder: "Validation"
status: published
created: 2021-10-04
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000119992
---

# *|Validation| CSK 7 SW/Win10 Compatibility Issue

If you are working with a CSK 7 site that is installed on a Windows 10 server and they get the following error in the logs when loading their license:


**Product license is invalid, 'License expired on 0001-01-01T00:00:00Z'**


We found that Windows 10 PCs have an incompatible time setting with CSK 7, which was resolved in CSK 8.
The solution for this would be to have the site upgrade to at least CSK 8 to get around this issue.