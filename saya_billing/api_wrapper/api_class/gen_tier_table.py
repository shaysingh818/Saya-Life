import location

locationclass = location.Locations("daca9c1f6ffdb7eb89b53165b477a0bda041aee8", "http://10.0.0.153:8000") 

def create_lot(county_lot_title, low, high, county): 
    locationclass.add_county_lot_size(county_lot_title, low, high, county) 
    return "Added title"  

def create_tier_lot(tier_level, county_lot_title, low, high): 
    locationclass.add_lot_tier(" {} : {} ".format(tier_level, county_lot_title), low, high, county_lot_title) 
    return "Added thing" 


create_lot("LA_Under_7500", 0, 7500, "LA_County") 
create_tier_lot("Tier 1", "LA_Under_7500", 0, 8)    
create_tier_lot("Tier 2", "LA_Under_7500", 9, 11)
create_tier_lot("Tier 3", "LA_Under_7500", 12, 17)
create_tier_lot("Tier 4", "LA_Under_7500", 18, 1000)


create_lot("LA_Under_10999", 0, 7500, "LA_County") 
create_tier_lot("Tier 1", "LA_Under_10999", 0, 8)    
create_tier_lot("Tier 2", "LA_Under_10999", 9, 12)
create_tier_lot("Tier 3", "LA_Under_10999", 13, 20)
create_tier_lot("Tier 4", "LA_Under_10999", 21, 1000)


create_lot("LA_Under_17499", 0, 7500, "LA_County") 
create_tier_lot("Tier 1", "LA_Under_17499", 0, 8)    
create_tier_lot("Tier 2", "LA_Under_17499", 9, 16)
create_tier_lot("Tier 3", "LA_Under_17499", 17, 32)
create_tier_lot("Tier 4", "LA_Under_17499", 33, 1000)


create_lot("LA_Under_43559", 0, 7500, "LA_County") 
create_tier_lot("Tier 1", "LA_Under_43559", 0, 8)    
create_tier_lot("Tier 2", "LA_Under_43559", 9, 18)
create_tier_lot("Tier 3", "LA_Under_43559", 19, 38)
create_tier_lot("Tier 4", "LA_Under_43559", 39, 100)


create_lot("LA_Over_43560", 0, 7500, "LA_County") 
create_tier_lot("Tier 1", "LA_Over_43560", 0, 8)    
create_tier_lot("Tier 2", "LA_Over_43560", 9, 18)
create_tier_lot("Tier 3", "LA_Over_43560", 16, 38)
create_tier_lot("Tier 4", "LA_Over_43560", 39, 100)
