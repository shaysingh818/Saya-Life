# Automated Billing Cycle

Understanding how billing item amounts are calculated, what are the variables involved in billing and automate the process.

## ACCOUNT NUMBER: 
Billing information requires an Account Number: Account number is needed for inquiring about billing or service regarding charges.

Interpretation: Billing system needs an account number associated with the Tenant in order to keep track of the service/billing. This could be implimented with accounts that have an account ID assoicated with it.  

Implementation: Account/Authentication User model that has account ID(Unique account identifier)

## ACCOUNT SUMMARY:
Tells how much the USER owes and when the payment is DUE. Account summary also breaks down how much the user owed in the PREVIOUS month. 

Interpretation: If we automate this process, we will need to make it so that the user can get a summary of their charges and see the billing cycle for the last couple of months. Any account ID could have an account summary associated with it. 

Implementation: Account/Authentication User Model can use an account summary field

## MESSAGES: 
Messages are sent about your account regarding events/water saving options/constructions and other things important for the user's account. 
IF the user exceeds the water bill limit, an alert appears to let them know. 

Interpretation: To my understanding, this is simply a notification system. This could be automated with a push notification/alert system. We can also put permission/category types on these notifications. Categories could include, Overdue Bill Alert, Exceed Limit Alert, Simple Bill Notification for information charges. 

Implementation: Push Notifications/Messaging system(Broad) 

## SERVICE CHARGES:
Fixed costs on a user's bill. Established to recover the fixed costs of IRWD’s water distribution system, treatment processes and sewers. 
This is the IRWD Water Distribution: https://www.irwd.com/services/water-supply-reliability

Interpretation: Service charges like Water and sewer service. Im assuming this would be the employees that work on the quality/usage of water to make it more efficient and keep the water clean etc. In order to automate this, the service charges would need to be sent/transparent

Implementation: Dynamic service charge calcluator. Figure out the fixed costs for service charges like water and sewer and add it to the bill. 

## BILLING DETAILS:
Billing Details section, is a breakout of the charges and data used in calculating your bill. This includes your meter size, your previous and current monthly meter readings, and the amount of water your household used during the billing period. 

Interpretation: This section calcuates your usage and determines the bill based on your water meter usage. This includes information about your water meter and how much water a tenant is using. This could be automated if we can send the values of the water usage to some sort of electronic service that can calculate billing details. 

## WATER USAGE CHARGES: 
Water usage charges are dynamic and VARY based on the amount of water someone uses. The rates depend on the Tier USAGE

#### Tier 1: 8 HCF OR 16 HCF on a BI Monthly basis(Basic indoor water use)
#### Tier 2: Indoor water usage(General, Irrigation, Drought tolerant landscapes)
#### Tier 3: Above average water usage, irrigation for a typical lawn
#### Tier 4: Excessive USE. Usage is way above the first 3 tiers

# Terminology (Hard to read on DOC) 

### Water Budget
### Outdoor Water Budget
### Indoor Water Budget
### Variances
### Water Usage Charges
### Pumping Searhcarge(Not sure if this is how it spelled, Font too small)
### Conservation Credit
### Sewer Service Charge
### Rebill Amount
### Net Amount
### Total Adjustments
