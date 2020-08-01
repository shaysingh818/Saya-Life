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

    #get all the tiers under a certain lot
    def get_lot_tiers(self, lot_title): 
        pass


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


    def create_lot(self,county_lot_title, low, high, county): 
        self.add_county_lot_size(county_lot_title, low, high, county) 
        return "Added title"  

    def create_tier_lot(self, tier_level, county_lot_title, low, high): 
        self.add_lot_tier(" {} : {} ".format(tier_level, county_lot_title), low, high, county_lot_title) 
        return "Added thing" 



