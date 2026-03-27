---
title: "*|CSH| - Configuring Access to Portal (Creating User Roles and Users)"
freshdesk_id: 17000064936
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host Portal / Configuration"
status: published
created: 2017-12-29
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000064936
---

# *|CSH| - Configuring Access to Portal (Creating User Roles and Users)

**Please Note: These are instructions for creating User Accounts/Roles and adjusting permissions, but support agents should follow the policy guidelines ****[here]**** when addressing customer access requests:**

# Configuring Access to Portal]


QSR Automations Enterprise Portal contains a suite of tools:


- ConnectSmart Host 

- ConnectSmart Portal Kitchen

- Guest View

- Team Assist

- Control Point


Anyone with permission to access the portal can log in and use any or all of the functionality available.  To maintain the integrity of settings or configurations, permissions are assigned to users.  Within this document, we will discuss what a User Role is and how to create one, how to add users and define the various permissions.  This will ensure that anyone who has access to the Enterprise Portal is only able to access the specific content defined in their role. 


## User Roles and Users]


Both User Roles and User profiles are configured at the Company level.  The initial user for any company defaults to System Admin.  This role is assigned during the creation of the company in Enterprise. 


To create additional roles log into the Company Level Portal:


1.   Select User Roles


2.   Select the to add a new User Role. 


3.  Name the Role.


4. Select the Permissions this role should have for the Portal. 


5. Select OK after all Permissions have been added to the role. 


**N****o****t****e****:****  **Explanations of each permission are in the Appendix below.


**Note:**  Site users configured at this level are only for users with ConnectSmart Host for Windows.  The process is the same for building both site and portal roles. 


## Adding Users]


To add users that will be assigned the roles just configured select the Users Menu in the left navigation pane.


Select add a User and complete a form for each user. 


Select the box next to Portal Access and assign a role for the user from the drop-down.


**N****o****t****e****:****  **Email verification is required for a Portal User.   


Select the Sites tab and chose the site or sites this user should have access to.


The Other tab has options for the user to be one of the Company Contacts, Subscribe to Quick tip emails, and/or the Daily Summary.  As a Company contact, this would add their email address to the distribution list for Enterprise updates or Maintenance from QSR Automations.  Quick tips are emailed periodically and contain quick training notes.  The Daily Summary email is auto-generated after the end of day and emailed out each morning.  The report contains summary information about the prior day’s business ConnectSmart Host information.  


The Concepts tab contains any concept that’s associated with the company.  These may be brands under a larger company or used for Team Assist configuration. 


Repeat these steps for all users requiring access to the Portal. 


Users will need to verify their email address and log into the Portal using the credentials configured on the form. 


If a user has access to multiple areas of the Portal provide the Company Level link for navigation purposes. 


To view Company Level and navigate to other areas of the Portal:


[http://portal.qsr.cloud/]


Kitchen Only:


[https://portal.kitchen.qsr.cloud/]


ConnectSmart Host  Only:


[https://portal.host.qsr.cloud/]


Team Assist Only:


[http://portal.teamassist.qsr.cloud/]


GuestView Only:


[http://portal.guestview.qsr.cloud/]


Control Point Only:


[https://portal.controlpoint.qsr.cloud]


# Site Only Users]


ConnectSmart Host for Windows has the option to configure Site Only users from the Portal.  A site user may be a host or member of management that never needs access to the Portal but needs varying levels of access to the DineTime Host client. 


From the ConnectSmart Host section of the Portal, choose a Site then Manage / Site Users. 


Fill out the form and select the Site role that best fits the needs of the user.  Site-level only users do not require an e-mail address. 


# Appendix]

## Portal Roles]

PermissionDefinitionView Company InsightThe ability to view reporting data at the company level.Edit Company ProfileAbility to change the company profile settings such as the name, address, and phone number.View Portal RolesView ONLY roles available at the Portal level.Edit Portal RolesModify existing Portal Roles or create new ones.View Site RolesView ONLY roles available to assign to Site Users.Edit Site RolesModify existing Site Roles or create new ones.View UsersView all users, no ability to modify or create new ones.Edit UsersModify existing Users or create new ones.Add ConceptA concept can be a smaller brand under a parent company or it can be a way to configure Team Assist in the Portal.  Adding a concept would be adding that at a company level for use in another way later.Delete ConceptRemoving a concept from the company.Edit ConceptMaking changes to a concept such as the name, website information, social media information, and cuisine that is displayed to consumers.Add TemplateA Template is a way to build ConnectSmart Host for Windows Customizations at a company level and then apply it across multiple sites.  This would allow the user to create a template.Delete TemplateRemove the template mentioned above.Edit TemplateMake changes to the template mentioned above.Apply TemplateIf a new ConnectSmart Host site is added, this would allow a template to be applied to that additional site.Edit Company Customize SettingsThe settings under customize at the company level are for Guest Book custom fields, Fixed guest notes that would appear on the Host Client, and Loyalty program setup and configuration.View Guest BookAbility to view the Company Guest Book.Add Guest RecordAbility to add a guest to the guest book.Delete Guest RecordRemove a Guest Record from the guest book.Edit Guest RecordMake updates to guest records which may include, phone number, email, or name information.Email CampaignsThe functionality behind this has been removedSites ListingAbility to view the list of all sites in the company.Add/Edit/Delete Kitchen DatasetsKitchen Datasets are created at the company level and then applied to individual sites.  This would allow the user to create new, change existing, or delete kitchen datasets.Apply Kitchen DatasetsWhen a new restaurant comes online with Enterprise Kitchen, this would allow the user to apply existing Kitchen Datasets to the new restaurant or any existing restaurant.Site – InsightsAbility to view Site Dashboard and Reports.  This would apply to software available on the site.  Either ConnectSmart Host, ConnectSmart Kitchen, or Both.Site – OperationsThis tab is for ConnectSmart Host sites and contains the Active Wait List, Guest Messages, and Reservation Book Functionality.Site – ManageThis tab is for ConnectSmart Host sites and contains site-specific information such as Operating Hours, Availability Plans, the ability to create Site Users, and other settings.  Access to this tab would allow for viewing and changing settings.Site - CustomizeThis tab is specific to ConnectSmart Host and contains all the customized settings that are also available to be built as a template.Site – Floor PlansThis tab is specific to ConnectSmart Host and allows access to view and/or modify Seating Areas, tables, floor plans, servers, and shifts.Stop Online BookingsThis functionality would turn off the ability for new reservations to be added while this is in place.Site - AlertsThis permission allows for the configuration of Alerts that can be sent to premise pagers or act as a pop-up notification on the Host Client.Override Reservation AvailabilityIf using reservation availability plans to manage reservation volume, this setting would allow an individual to override any setting, including the size of the party, and the ability to make a reservation beyond capacity.Override Reservation SizeThis would only allow the user to accept a reservation whose party size is greater than the configured large party size.


## Site Roles]

PermissionDefinitionView Guest BookView Only permission for Guest Book.Add Guest RecordAbility to build a new guest profile.Delete Guest RecordRemoving an existing Guest Profile.Edit Guest RecordEditing a current guest book entry.  This could include changing a telephone number or address.View ServersThe Server list is available at the Host Stand so it can be applied to shifts to serve guests.  This would allow the user to view that list but take no action.Add ServerAbility to create a new server profile at the host stand.Delete ServerRemoving an existing Server profile.Edit Server (Name Fields)Ability to edit a server’s Name Only.Edit Server (Contact Fields)Ability to edit a server’s phone number or email address.Edit Server (ID Fields)Ability to edit a server’s external ID.View Floor PlansView only floor plans in the ConnectSmart Host Client.Floor Plans-Add TablesAbility to add tables to the floor plan(s) in ConnectSmart Host Client.Floor Plans-Delete TablesAbility to Delete Tables from the floor plan(s) in ConnectSmart Host Client.Floor Plans-Edit TablesAbility to Edit settings to existing tables on the floor plan(s) in ConnectSmart Host Client.Add Floor PlansCreating a new floor plan for use.Delete Floor PlansDelete any existing floor plansEdit Floor PlansEdit Existing Floor Plans / move tables/change preferences on tables/size and shape of tables.
All of the Floor Plan permissions would be a permanent change to the floor plan, not just to a shift.View ShiftsView existing shifts for use in ConnectSmart Host.Add ShiftsCreate new shifts for use in ConnectSmart Host.Delete ShiftsRemoving shifts permanently.Edit ShiftsModify existing shifts.  This could include expanding or shrinking table sections or adding a second server to a section.Change Active ShiftThis setting allows the user to change or reset a shift back to its default.  This can be useful if tables move around frequently or if a host is there for a Server Shift changeView Reservation BookView only any reservations from the reservation book on ConnectSmart Host.Add ReservationCreate a new reservation at the Host Stand.Cancel ReservationCancel a reservation from the Host Stand.Edit ReservationModify an existing reservation, including party size, time, and any preferences or notes.Edit UsersMake changes to existing users' profiles.Sign OutAbility to sign out of the ConnectSmart Host Client.  This can be useful if the permissions of a user are restricted and a function they are not allowed to complete is needed.Shutdown the ClientAbility to Exit the ConnectSmart Host Client on an iPad or a Windows touch device.Settings – AllModify settings within the ConnectSmart Host Client.Settings – Visit Quick NotesAdd or modify existing Quick Notes from the Host Client.
*All Settings permissions are through the menu on the Host Client.Settings – Greeter Form ActionsAbility to modify which greeter form to use and how the greeter form responds to actions on the Host Client.Settings – Quote MethodModify the quoting method being used and how the quote will be presented when on a waitlist.Settings – Chit PrintingIf configured for Printing from ConenctSmart this setting would allow the user to modify when the chit would print.Settings – Chit LayoutsIf configured for Printing from ConnectSmart this setting would allow the user to modify the Chit itself.Settings-Table TurnsConfiguring this setting at the client was removed.Settings – Suggested SeatingAbility to configure how many suggested tables will display for the shift and the Section rotation rule for Server rotations.Override Reservation AvailabilityIf using reservation availability plans to manage reservation volume, this setting would allow an individual to override any setting, including the size of the party, and the ability to make a reservation beyond capacity.Override Reservation SizeThis would only allow the user to accept a reservation whose party size is greater than the configured large party size.In-Client ReportingThis would place an additional option on the menu page of the client to run reports for ConnectSmart Host and/or ConnectSmart Kitchen.Allow User to be paged via SMSThis would allow a user to be SMS texted directly from the ConnectSmart Host Client.  There are additional steps required for this to work properly.  It starts with this setting.