---
title: "*|POS| - Common Field Mappings By POS"
freshdesk_id: 17000098474
category: "Internal Only"
folder: "POS Configuration"
status: published
created: 2019-12-17
updated: 2023-11-03
views: 0
tags: ["Field Mapping"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000098474
---

# *|POS| - Common Field Mappings By POS

**MICROS:**


 


QSR FIELDMICROS FIELDItem IDMenu ItemDepartment NumberPrint Class or Family or Major Group(Depending on TSConnect Settings)Item CategoryPrint Class or Family or Major Group(Depending on TSConnect Settings)Seat NumberSeat NumberTable NameTable NumberServer NameServer NameTransaction NumberCheck NumberDestination IDOrder TypeCustomer NameGuest Check ID


**ALOHA:**


QSR FIELDALOHA FIELDItem IDMenu Item PLUDepartment NumberVideo Group IDItem CategorySales CategoryItem PriorityItem PriorityCook TimeDelay TimeDestination IDOrder ModeCustomer NameOrder NameTable NumberTable IDSeat NumberPivot Number


**FOCUS:**


**      **

QSR FIELDFOCUS FIELDItem IDInternal ID NumberDepartment NumberPrint GroupItem CategoryReport GroupDestination IDOrder TypeTransaction NumberCheck NumberTerminal NumberStation NumberTable NumberTable NumberServer IDAccess CodeCourseMeal StageServer NameNicknameSeat NumberPositionCook TimeCook TimePriority ValuePriority


**FUTURE:**


**      **

QSR FIELDFUTURE FIELDItem IDItem.VUIDDepartment NumberDepartment.VUIDItem Category
Destination IDSale.OrderTypeCook TimeItem.PrepTime


**PIXEL:**


**       **

QSR FIELDPIXEL FIELDItem IDProduct.ProdNumDepartment NumberProduct.ReportNoItem Category
Destination IDSalesType.SaleTypeIndex


**SILVERWARE:**


**     **

QSR FIELDSILVERWARE FIELDItem IDItem.MenuItemIdDepartment NumberItem.departmentIdItem Category
Destination IDPosOrder.destinationTransaction NumberPosOrder.qsrNumber


**INFOGENESIS: **


**       **

QSR FIELDINFOGENESIS FIELDItem IDItem IDDepartment NumberKitchen Video DepartmentItem CategoryKitchen Video CategoryDestinationCheck Type ID


**BRINK:**


** **

QSR FIELDBRINK FIELDItem IDItem IDDepartment NumberVideo Group IDItem CategoryRevenue Center IDTerminal NumberTerminal IDDestination IDDestination IDTable Order Name


**EMAGINEPOS:**


**      **

QSR FIELDEMAGINEPOS FIELDItem IDQSRItemIDDepartment NumberQSRDepartmentIDItem Category
Destination IDQSRDestinationIDPriority ValueItem Print Priority


**POSITOUCH:** 


**      **

QSR FIELDPOSITOUCH FIELDItem IDInventory NumberDepartment NumberPrep Category, Major or Minor CategoryItem CategoryPrep Category, Major category, Minor Category or ZeroTerminal NumberTerminal NumberSeat NumberSeat NumberTable NumberTable NumberServer NameServer NameDestination IDCost CenterTransaction NumberCheck NumberCook TimePrep MinutesCustomer NameCustomer “Name” item


**SQUIRREL:**


QSR FIELDSQUIRREL FIELDItemID PLU or MenuID (x2 if positive or abs(x2)+1 if odd) if no PLU
Destination DepartmentIndex or LogicalPrinterLetterDepartment Number Item Major Category or PLU Lookup value or Logical Printer Letter or configured KDS department or Physical Printer letter 


**DIGITAL DINING:**


QSR FIELDDIGITAL DINING FIELDItem IDPLUDepartment NumberPrep TypeItem Category
Transaction NumberCheck NumberTerminal NumberRegister IDDestination IDProfit CenterCook TimePrep Time


**HEARTLAND:**

**QSR FIELD****Heartland Field**Check Number Check NumberCheck Number Ticket Number
Pickup Time
Hold Date
Scheduled Pickup Time Promised Date
Destination ID
Room ID
Terminal
Device Name, Device ID Item ID Item ID Department Display Group ID 


**ZONAL:**

**QSR FIELD****ZONAL FIELD**Transaction Number Transaction Number Course
Generated on fly by POS not stored
ItemID
(SubCateg)Index No+EntityCode
Department Number
PrintStreamID
Item Category (Can be 0)
Index No