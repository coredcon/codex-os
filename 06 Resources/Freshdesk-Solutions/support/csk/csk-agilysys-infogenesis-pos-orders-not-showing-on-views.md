---
title: "*|CSK| - Agilysys InfoGenesis POS orders not showing on views"
freshdesk_id: 17000124121
category: "Support"
folder: "CSK"
status: published
created: 2022-03-18
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000124121
---

# *|CSK| - Agilysys InfoGenesis POS orders not showing on views

Issue:


All QSR configuration is correct, but InfoGenesis POS is not sending orders


Solution:


infogene.ini located under the terminal profile settings should contain the IP address of the QSR server. This file can change based on the Windows profile the user is logged in under as well. Once the infogene.ini file is corrected with the correct QSR IP address and saved, the POS terminals will need to be reloaded to apply the setting change from the InfoGenesis server.