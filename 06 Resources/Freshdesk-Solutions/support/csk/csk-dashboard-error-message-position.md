---
title: "|CSK| Dashboard Error Message Position"
freshdesk_id: 17000142983
category: "Support"
folder: "CSK"
status: published
created: 2024-10-14
updated: 2024-10-14
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000142983
---

# |CSK| Dashboard Error Message Position

Issue: View error messages are appearing at the bottom of the view, blocking the touch panel controls as seen below:


This is caused by setting the dashboard's Default View ID to a specific view when the view is set to not show the View Header. This is not recommended when using the dashboard simply as a touch panel. Setting the View ID is relevant when using a dashboard for metrics specifically tied to a particular view. 


In order to resolve this without turning on the View Header, you can double-click the touch panel in the View Editor, and set the Default View ID to "0-None."


This will then result in the error appearing only at the top of the view: