
### Register Billing
Get: Not allowed   
Post: Register User: Username and Password required. 

Params = {  
	'username': username,    
	'password': password,    
	'password2': password    
}   

```
/billing/register/
```

### View all States on billing system

Get: Get all registered States on the billing system  

```
/billing/states/states/
```

### View individual state and create county under State
Get: Get individual State Object   
Post: Create County Under State object  

```
/billing/states/state/<state_id>/
```


### View all counties on billing system
```
/billing/counties/counties/
```

### View indidividal county
```
/billing/counties/<county_id>/ 
```


### View all the counties in a State
```
/billing/counties/county-state/<state_id>/
```
