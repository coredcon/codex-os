---
title: "|Internal Only| - How to Check if Site is Eligible for Technical Support"
freshdesk_id: 17000139883
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2024-04-04
updated: 2024-08-07
views: 0
tags: ["License", "End of Life", "Salesforce"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000139883
---

# |Internal Only| - How to Check if Site is Eligible for Technical Support

### **Find the site in Salesforce**


- May need to ask for address, if having hard time try finding in google first then copying address listed.**
**

### **Is the Site a Red Robin Location?**


- If it is a Red Robin, check if its parent account is either "Restaurant Development Company of Medford LLC" or "Infinity RRGB Ventures Inc" they are currently supported and should reflect this in Salesforce with a SaaS subscription.

- If it is a Red Robin that is a Corporate site or any other franchise than listed above, please continue with the listed policies below to verify if they are on SaaS or have valid software maintenance. If they are not we do not support them.

### **Determine if site is using Asset or Subscription License**


- Asset License will be first block in Salesforce, and will list a version that is maximum version site is allowed to use.

- Subscription will be Second Block (Below Asset) and allows the site to use any supported version of CSK/Host.

- For sites with more than 10 entries in either of Asset or Subscription you will need to select View All Option to see full list.

### **Asset Sites**


- Sometimes referred to as Perpetual License

- MUST HAVE A **VALID **"ConnectSmart Kitchen Annual Software Maintenance" Subscription to be eligible for Support

- A Valid Software Maintenance Subscription will have a Next Billing Date for End of Current Year


- Picture Below shows site with a Asset License for up to CSK 2020 and a valid Software Maintenance Subscription.


### **Subscription Sites**


- Sometimes referred to as SaaS.

- Does NOT need any Software maintenance for support

- Below picture shows active CSK subscription


- On some sites you will see a subscription with a Disabled or Expired Status. This is not a valid subscription and the site will need either an Asset or Subscription listed somewhere else that is valid.

- Notice the Disabled Status in picture below - This would not be supported and we would direct any questions about this towards Account/Channel Manager.


### **Once You See Sites License Is Supported - Check the _Actual_ Version They Use**


- From Salesforce copy the Site ID(Located below the Site Name and next to Store Number) and search for it in Admin Portal -> Sites.

- In the picture below you can see where the Last Check In Date and Last CSK Version is listed.

- If you leave Admin Portal logged in you may need to either open the actual site page to get updated info as search will only reflect the database at time of your last log in.