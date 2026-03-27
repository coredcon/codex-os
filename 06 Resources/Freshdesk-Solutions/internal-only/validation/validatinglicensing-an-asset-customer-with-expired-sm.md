---
title: "Validating/Licensing an Asset Customer with Expired SM"
freshdesk_id: 17000139062
category: "Internal Only"
folder: "Validation"
status: published
created: 2024-02-18
updated: 2024-02-18
views: 0
tags: ["Asset", "Expired SM"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000139062
---

# Validating/Licensing an Asset Customer with Expired SM

If SM is expired and a re-validation request is received, the new license may only be created with the same version that is on the old/current license so long as that version is a supported version.  The license may not be upgraded, regardless of the version present in SF.


 


Example #1


 


SF shows an Asset CSK product with version 2022 and expired SM.  Customer is requesting to upgrade from CSK 2019 to CSK 2022.  Both CSK 2019 and CSK 2022 are supported versions, but upgrades are not allowed with expired SM.  In this example you would only be able to re-validate for CSK 2019 and then refer customer to ClientServices or PartnerAssist for further assistance.


 


Example #2


 


SF shows an Asset CSK product with version 2019 and expired SM.  Customer is requesting a re-validation with CSK 2019 on the license.  You check the old/current license and see it only contains CSK 8.  A new license is not allowed as it could only be created with CSK 8 and CSK 8 is no longer supported.  Please refer customer to ClientServices or PartnerAssist for further assistance.


 


Example #3


 


SF shows an Asset CSK product with version 2019 and expired SM.  Customer is requesting a re-validation for CSK 2019.  You check the old/current license and see it contains CSK 2019.  A new license is allowed as 2019 is a supported version.


 


There are likely many more examples out there.  The key takeaway is this: an Asset customer with expired SM may only be re-validated for the version of CSK on the old/current license and only if that version is a supported version.


_Published by Nathan Walk_


_02/15/24_