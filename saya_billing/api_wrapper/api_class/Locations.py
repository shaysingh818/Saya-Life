import requests
import os
import json


class Locations: 

    def __init__(self, token, url): 
        self.token = token
        self.url = url

    def get_all_states(self):
        pass


    def get_state_counties(self, state_code):

        headers = {
                "Authorization": "Token {}".format(self.token) 
                }

        data_request = requests.get("{}/billing/locations/state-counties/{}/".format(self.url, state_code), headers=headers) 

        return data_request.text

    def get_state_counties_json(self, state_code):

        headers = {
                "Authorization": "Token {}".format(self.token) 
                }

        data_request = requests.get("{}/billing/locations/state-counties/{}/".format(self.url, state_code), headers=headers) 

        return data_request.json()


    def get_county_lot_sizes(self, title): 
        headers = {
                "Authorization": "Token {}".format(self.token) 
                }

        data_request = requests.get("{}/billing/locations/county-lots/{}/".format(self.url, title), headers=headers) 

        data_request = data_request.json() 
        return data_request.text


    def get_county_lot_sizes_json(self, title): 
        headers = {
                "Authorization": "Token {}".format(self.token) 
                }

        data_request = requests.get("{}/billing/locations/county-lots/{}/".format(self.url, title), headers=headers) 

        data_request = data_request.json() 
        return data_request.json() 



    def add_county_lot_size(self, title, lot_low, lot_high, county_title):
        
        headers = {
                "Authorization": "Token {}".format(self.token) 
                }

        data = {
                'title': title,
                'lot_size_low': lot_low,
                'lot_size_high': lot_high
                }

        data_request = requests.post("{}/billing/locations/county-lots/{}/".format(self.url, county_title), data=data, headers=headers) 

        return data_request.json()
    
    def add_lot_tier(self, title, lot_low, lot_high, lot_size):
        
        headers = {
                "Authorization": "Token {}".format(self.token) 
                }

        data = {
                'title': title,
                'tier_range_low': lot_low,
                'tier_range_high': lot_high
                }

        data_request = requests.post("{}/billing/locations/county-tiers/{}/".format(self.url, lot_size), data=data, headers=headers) 

        text_response = data_request.text

        return text_response

   
location = Locations("daca9c1f6ffdb7eb89b53165b477a0bda041aee8", "http://10.0.0.153:8000") 

#print(location.add_county_lot_size("CA_Under_7500", 0, 7500, "LA_County")) 
#print(location.add_lot_tier("Tier_1", 0, 8, "CA_Under_7500")) 
print(location.get_county_lot_sizes("LA_County"))


#This is the dynamic way to add a county, add the county lot size parameter, and then add property tiers for it
def tier_allocation(county, county_lot_title, county_prop_low, county_prop_high, tier_level, tier_low, tier_high):
   lot_size_parameter = location.add_county_lot_size(county_lot_title, county_prop_low, county_prop_high, county)
   lot_title = lot_size_parameter["title"] 
   location.add_lot_tier(tier_level.format(lot_title), tier_low, tier_high, lot_title) 


#if you want to add the values manually this is how you can do it. 
def replicate_table(county):
    #First row
    ca_under_7500 = location.add_county_lot_size("CA_Under_75034", 0, 7500, county)
    lot7500 = ca_under_7500["title"]
    location.add_lot_tier("Tier_1_{}".format(lot7500), 0, 8, lot7500)
    location.add_lot_tier("Tier_2_{}".format(lot7500), 9, 11, lot7500) 
    location.add_lot_tier("Tier_3_{}".format(lot7500), 12, 17, lot7500) 
    location.add_lot_tier("Tier_4_{}".format(lot7500), 17, 50, lot7500) 

    ca_under_10999 = location.add_county_lot_size("CA_Tier_Lot2", 7500, 10999, county)
    lot10999 = ca_under_10999["title"]
    location.add_lot_tier("Tier_1_{}".format(lot10999), 0, 8, lot10999)
    location.add_lot_tier("Tier_2_{}".format(lot10999), 9, 12, lot10999)
    location.add_lot_tier("Tier_3_{}".format(lot10999), 13, 20, lot10999)
    location.add_lot_tier("Tier_4_{}".format(lot10999), 20, 100, lot10999)

    ca_under_17499 = location.add_county_lot_size("CA_Tier_Lot3", 11000, 17499, county)
    lot17499 = ca_under_17499["title"]
    location.add_lot_tier("Tier_1_{}".format(lot17499), 0, 8, lot17499)
    location.add_lot_tier("Tier_2_{}".format(lot17499), 9, 16, lot17499)
    location.add_lot_tier("Tier_3_{}".format(lot17499), 17, 32, lot17499)
    location.add_lot_tier("Tier_4_{}".format(lot17499), 32, 1000, lot17499)

    ca_under_43559 = location.add_county_lot_size("CA_Tier_Lot4", 17500, 43559, county)
    lot43559 = ca_under_43559["title"] 
    location.add_lot_tier("Tier_1_{}".format(lot43559), 0, 8, lot43559)
    location.add_lot_tier("Tier_2_{}".format(lot43559), 9, 18, lot43559)
    location.add_lot_tier("Tier_3_{}".format(lot43559), 19, 38, lot43559)
    location.add_lot_tier("Tier_4_{}".format(lot43559), 38, 100, lot43559)

    ca_under_43560 = location.add_county_lot_size("CA_Tier_Lot5", 43560, 100000, county)
    lot43560 = ca_under_43560["title"] 
    location.add_lot_tier("Tier_1_{}".format(lot43560), 0, 8, lot43560)
    location.add_lot_tier("Tier_2_{}".format(lot43560), 9, 18, lot43560)
    location.add_lot_tier("Tier_3_{}".format(lot43560), 19, 38, lot43560)
    location.add_lot_tier("Tier_4_{}".format(lot43560), 38, 1000, lot43560)

    #location.add_county_lot_size("CA_Tier_Lot3", 11000, 17499, county)
    #location.add_county_lot_size("CA_Tier_lot4", 17500, 43559, county)
    #location.add_county_lot_size("CA_Tier_lot5", 43560, 100000, county)

replicate_table("LA_County")

