import location

locationclass = location.Locations("764950e00100dae7d9a32659c9af73d15c2879ae", "http://10.0.0.153:8000") 

locationclass.create_lot("LA_Under_7500", 0, 7500, "LA_County") 
locationclass.create_tier_lot("Tier 1", "LA_Under_7500", 0, 8)    
locationclass.create_tier_lot("Tier 2", "LA_Under_7500", 9, 11)
locationclass.create_tier_lot("Tier 3", "LA_Under_7500", 12, 17)
locationclass.create_tier_lot("Tier 4", "LA_Under_7500", 18, 1000)


locationclass.create_lot("LA_Under_10999", 7500, 10999, "LA_County") 
locationclass.create_tier_lot("Tier 1", "LA_Under_10999", 0, 8)    
locationclass.create_tier_lot("Tier 2", "LA_Under_10999", 9, 12)
locationclass.create_tier_lot("Tier 3", "LA_Under_10999", 13, 20)
locationclass.create_tier_lot("Tier 4", "LA_Under_10999", 21, 1000)


locationclass.create_lot("LA_Under_17499", 11000, 17499, "LA_County") 
locationclass.create_tier_lot("Tier 1", "LA_Under_17499", 0, 8)    
locationclass.create_tier_lot("Tier 2", "LA_Under_17499", 9, 16)
locationclass.create_tier_lot("Tier 3", "LA_Under_17499", 17, 32)
locationclass.create_tier_lot("Tier 4", "LA_Under_17499", 33, 1000)


locationclass.create_lot("LA_Under_43559", 17500, 43559, "LA_County") 
locationclass.create_tier_lot("Tier 1", "LA_Under_43559", 0, 8)    
locationclass.create_tier_lot("Tier 2", "LA_Under_43559", 9, 18)
locationclass.create_tier_lot("Tier 3", "LA_Under_43559", 19, 38)
locationclass.create_tier_lot("Tier 4", "LA_Under_43559", 39, 100)


locationclass.create_lot("LA_Over_43560", 43560, 100000, "LA_County") 
locationclass.create_tier_lot("Tier 1", "LA_Over_43560", 0, 8)    
locationclass.create_tier_lot("Tier 2", "LA_Over_43560", 9, 18)
locationclass.create_tier_lot("Tier 3", "LA_Over_43560", 16, 38)
locationclass.create_tier_lot("Tier 4", "LA_Over_43560", 39, 100)
