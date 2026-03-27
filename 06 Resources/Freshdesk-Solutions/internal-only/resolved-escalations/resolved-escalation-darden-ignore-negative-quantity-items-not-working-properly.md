---
title: "*|Resolved Escalation| - DARDEN - Ignore Negative Quantity Items not working properly"
freshdesk_id: 17000077835
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-09-06
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000077835
---

# *|Resolved Escalation| - DARDEN - Ignore Negative Quantity Items not working properly

(09/06) - CC - CSK 8.0 released 06/26/18 addressed this issue


Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/tickets/133908]


> On Fri, 4 May at 8:45 AM , QSR Support Team <supportteamdistro@qsrautomations.com> wrote:Team, Please see the escalation, below. 
**Severity:** Normal**Customer:** POS Canada**Company ID:** POS Canada**Location / SiteID:** Waterfront River Pub & Terrace**Location Found:**_Production_**Product:** ConnectSmart Kitchen**Component:** Kitchen Server**Version:** 7.2.116**Support Ticket #:** 132557**Date Reported:**05/03/18 **Account Manager:** Ty Reed  **ISSUE**:   Ignore Negative Quantity option in Transaction Manager is not working properly. This POS of Canada client has the option in Transaction Manager selected to ignore negative quantity items, however when they send orders with negative quantity from the POS there are instances of the orders displaying on their kitchen stations. Client advised that the site is using Pixel Point and when they split checks and void the split check it sends negative quantities (this is a known bug with Pixel that the POS developers state will not be fixed) which in the past the client stated that is the reason they would use a connect app for the ignore Negative Item Quantities before it was built into CSK.  We tested in our lab and were able to recreate the issue but did find that when coursing is turned off on the activity level the negative quantities no longer display on the stations. **STEPS TO REPRODUCE** 1.       Load attached Dataset “Dataset - POS Canada – 132557”2.       Play attached Capture “Negative Quantity Transaction Capture - POS Canada – 132557”3.       Verify that on the both the order view and item view stations the negative quantity item appeared (screenshot below):a.         Note: We did find that disabling coursing caused the negative items to not display. **ATTACHMENTS:** ·         Dataset the site is using.·         Capture of order sent with negative quantity·         Capture of the standard check splitting procedure the site utilizes that causes a negative quantity to be sent. **IMPACT:**  Sumegh from POS Canada advised that this site is using Pixel Point and when the split checks this causes the POS to send a report order for a negative quantity so this does cause some confusion in the kitchen. **WORKAROUND:**  Turning off Coursing does allow this setting to work, but the site uses Coursing extensively.