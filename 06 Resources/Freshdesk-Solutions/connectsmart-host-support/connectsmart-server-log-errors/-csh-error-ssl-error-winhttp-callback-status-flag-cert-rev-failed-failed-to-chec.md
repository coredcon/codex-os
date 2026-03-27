---
title: "* |CSH| -  Error: 'SSL Error: WINHTTP_CALLBACK_STATUS_FLAG_CERT_REV_FAILED failed to check revocation status.'"
freshdesk_id: 17000105569
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Log Errors"
status: published
created: 2020-06-19
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000105569
---

# * |CSH| -  Error: "SSL Error: WINHTTP_CALLBACK_STATUS_FLAG_CERT_REV_FAILED failed to check revocation status."

**Issue**:


During Registration or Check-In, QSR Product logs:
SSL Error: WINHTTP_CALLBACK_STATUS_FLAG_CERT_REV_FAILED failed to check revocation status.  


This can prevent the product from successfully registering and/or pulling down its license from Enterprise.


**Solution / Explanation: **


This occurs in version 2020. x and later when the appropriate endpoints for certificate revocation have not been allowed in the customer's network security.


See: [https://qsrautomations.freshdesk.com/a/solutions/articles/17000105567]