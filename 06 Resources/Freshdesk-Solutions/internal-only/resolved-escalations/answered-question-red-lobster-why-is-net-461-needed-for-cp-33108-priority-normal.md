---
title: "*|Answered Question| - RED LOBSTER - Why is .NET 4.6.1 needed for CP 3.3.108 - Priority: Normal"
freshdesk_id: 17000069641
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-04-03
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069641
---

# *|Answered Question| - RED LOBSTER - Why is .NET 4.6.1 needed for CP 3.3.108 - Priority: Normal

The feature in 3.3 that required ControlPoint Server to move up to .Net Framework version 4.6.1 from .Net Framework version 4.0 was adding support for LRS Table Locator 2.0 API. The LRS table locator API required websockets which were not supported in .net version 4.0.


> On Mon, 12 Feb at 4:38 PM , QSR Support Team <supportteamdistro@qsrautomations.com> wrote:Team,
 Please see the escalation, below.
 
**Severity:** Normal**Customer:** Red Lobster**Company ID:** Red Lobster**Location / SiteID:** Red Lobster Lab**Product:** ConnectSmart**Component:** ControlPoint**Version:** 3.3.108**Support Ticket #:** 126388**Customer:** Steve McCormick
 
 **QUESTION:**
 Why is .NET 4.6.1 required for ControlPoint 3.3.108?