import location

locationclass = location.Locations("9b17f7231219a0c94c54060ef510c7086cf0b4ef", "http://10.0.0.153:8000") 

locationclass.create_lot("LA_Under_7500", 0, 7500, "LA_County") 
locationclass.create_tier_lot("Tier 1", "LA_Under_7500", 0, 9, 5)    
locationclass.create_tier_lot("Tier 2", "LA_Under_7500", 9, 12, 7)
locationclass.create_tier_lot("Tier 3", "LA_Under_7500", 12, 18, 8)
locationclass.create_tier_lot("Tier 4", "LA_Under_7500", 18, 1000, 9)


locationclass.create_lot("LA_Under_10999", 7500, 10999, "LA_County") 
locationclass.create_tier_lot("Tier 1", "LA_Under_10999", 0, 9, 5)    
locationclass.create_tier_lot("Tier 2", "LA_Under_10999", 9, 13, 7)
locationclass.create_tier_lot("Tier 3", "LA_Under_10999", 13, 21, 8)
locationclass.create_tier_lot("Tier 4", "LA_Under_10999", 21, 1000, 9)


locationclass.create_lot("LA_Under_17499", 11000, 17499, "LA_County") 
locationclass.create_tier_lot("Tier 1", "LA_Under_17499", 0, 9, 5)    
locationclass.create_tier_lot("Tier 2", "LA_Under_17499", 9, 17, 7)
locationclass.create_tier_lot("Tier 3", "LA_Under_17499", 17, 33, 8)
locationclass.create_tier_lot("Tier 4", "LA_Under_17499", 33, 1000, 9)


locationclass.create_lot("LA_Under_43559", 17500, 43559, "LA_County") 
locationclass.create_tier_lot("Tier 1", "LA_Under_43559", 0, 9, 5)    
locationclass.create_tier_lot("Tier 2", "LA_Under_43559", 9, 19, 7)
locationclass.create_tier_lot("Tier 3", "LA_Under_43559", 19, 38, 8)
locationclass.create_tier_lot("Tier 4", "LA_Under_43559", 38, 100, 9)


locationclass.create_lot("LA_Over_43560", 43560, 100000, "LA_County") 
locationclass.create_tier_lot("Tier 1", "LA_Over_43560", 0, 9, 5)    
locationclass.create_tier_lot("Tier 2", "LA_Over_43560", 9, 19, 7)
locationclass.create_tier_lot("Tier 3", "LA_Over_43560", 19, 39, 8)
locationclass.create_tier_lot("Tier 4", "LA_Over_43560", 38, 100, 9)
