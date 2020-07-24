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

## WATER USAGE CHARGES: (Automated Water Charges Based on TIER's 1-4)  
Water usage charges are dynamic and VARY based on the amount of water someone uses. The rates depend on the Tier USAGE

#### Tier 1: 8 HCF OR 16 HCF on a BI Monthly basis(Basic indoor water use)
#### Tier 2: Indoor water usage(General, Irrigation, Drought tolerant landscapes)
#### Tier 3: Above average water usage, irrigation for a typical lawn
#### Tier 4: Excessive USE. Usage is way above the first 3 tiers

Implementation: Based on amounts of water used based on HCF/CCF we could automate assigning a tier level of water usuage. If a tenant has a high amount of water usage we can assign it either Tier 2-4. If the user is using water for an appartment/home, we could assign their usuage to tier 1 category. We could even categorize users on thier tier usage and focus on high tier usage to save water. 

# Terminology (Hard to read on DOC) 

1.) Water Budget  
2.)Outdoor Water Budget  
3.)Indoor Water Budget  
4.)Variances  
5.)Water Usage Charges  
6.)Pumping Searhcarge(Not sure if this is how it spelled, Font too small)   
7.)Conservation Credit  
8.)Sewer Service Charge  
9.)Rebill Amount  
10.)Net Amount  
11.)Total Adjustments   


## Los Angeles Country Waterworks 

#### How to pay bill?
Your water bill can be paid online using MyWAM, in person at your local District office, over the phone by calling 1-877-637-3661, or by mail.

If you wish to pay after regular business hours, drop your payment with the payment stub in the overnight deposit box located at the entrance of the District office.

Mailing your payment:
Enclose the detachable bottom portion of your bill, along with a check or money order for the amount due, in the envelope provided to ensure speed and efficiency in processing. Please do not include cash or coins. Please allow 7 to 10 business days for your payment to be received and posted on your account.

If the envelope provided is lost, please mail your payment to the following address:
Los Angeles County Treasurer
P.O. Box 512150
Los Angeles, CA 90051-0150


#### When is the bill due

Your water bill is due and payable upon presentation. You have 25 days from the date the bill is prepared to make your payment before the bill is delinquent. Bills that are delinquent are subject to a $10.00 late fee. A $33.00 fee is charged to cover processing costs for all returned checks.

#### How many gallons are represented be each unit
Each billing unit is 100 cubic feet of water which is equal to 748 gallons.


### Water rates for certain areas
|Waterworks District| Billing Code|
|-------------------|-------------|
|Marina del Rey Water| F17, 117,  W17| 
|District NO. 21, Kagel Canyon| 101, W01| 
|Dist 29, Malibu| F03, F05, F07, F09, I03, I05, I07, I09, W03, W05, W07, W09| 
| District No. 36, Val Verde| F12, I12, W12, W14|
|District No. 37, Acton| F15, I15, W15|
|District No. 40, Antelope Valley| NONE|

## RESOURCES
1.) https://www.irwd.com/services/water-supply-reliability
2.) https://dpw.lacounty.gov/wwd/web/MyWAM/OnlineBilling.aspx

