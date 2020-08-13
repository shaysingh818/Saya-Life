from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from locations.models import State, County
from .tier_model import LotSize, Tier
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from .tier_charge_model import Bill, Charge


class Property(models.Model): 
    title = models.CharField(max_length=100) 
    address = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    lot_size = models.IntegerField() 
    date_posted = models.DateTimeField(default=timezone.now) 
    hcf_usage = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    county = models.ForeignKey(County,on_delete=models.CASCADE) 

    class Meta: 
        ordering = ['date_posted'] 

    def __str__(self): 
        return 'Property {}'.format(self.title) 


class ProfileManager(models.Manager):

    def get_profile(self, pk): 
        try:
            return Profile.objects.get(pk=pk) 
        except Profile.DoesNotExist: 
            raise Http404

    def get_hcf_usage(self, pk): 
        user_profile = self.get_profile(pk=pk) 
        prop = user_profile.user_property
        hcf_water = prop.hcf_usage
        return hcf_water

    def get_hcf_gallons(self, pk):
        user_profile = self.get_profile(pk=pk) 
        hcf_usage = self.get_hcf_usage(user_profile.pk) 
        return hcf_usage * 748

    def display_county_charges(self, pk):
        user_profile = self.get_profile(pk=pk)
        charges = Charge.objects.filter(county=user_profile.county)
        list_charges = [] 
        for charge in charges: 
            list_charges.append("{}: {}".format(charge.title, charge.charge_amount)) 
        return list_charges


    def get_user_county_charges(self, pk):
        user_profile = self.get_profile(pk=pk)
        charges = Charge.objects.filter(county=user_profile.county)
        return charges

    def get_county_charge_total(self, pk): 
        user_profile = self.get_profile(pk) 
        charges = Charge.objects.filter(county=user_profile.county) 
        charge_sum = 0
        for charge in charges: 
            charge_sum += charge.charge_amount
        return charge_sum
        
    def get_property_tier_usage(self, pk):
        user_profile = self.get_profile(pk=pk)
        prop = user_profile.user_property
        hcf_water = prop.hcf_usage
        lot_size = int(prop.lot_size)
        county_lot_ranges = LotSize.objects.filter(county=user_profile.county)
        for lot in county_lot_ranges:
            if lot_size in range(lot.lot_size_low, lot.lot_size_high):
                hcf_tiers = Tier.objects.filter(lot_size=lot)
                for tier in hcf_tiers:
                    if hcf_water in range(tier.tier_range_low, tier.tier_range_high):
                        return tier

    def charge_tier_usage(self, pk):
        profile = Profile.objects.get(pk=pk)
        prop = profile.user_property
        hcf_water = prop.hcf_usage
        lot_size = prop.lot_size
        county_lot_ranges = LotSize.objects.filter(county=profile.county)
        tier_usage = self.get_property_tier_usage(profile.pk)
        charge_sum = 0
        final_charge = 0
        for lot in county_lot_ranges:
            if lot_size in range(lot.lot_size_low, lot.lot_size_high):
                hcf_tiers = Tier.objects.filter(lot_size=lot)
                subtract = hcf_water
                for tier in hcf_tiers:
                    if(subtract > 0):
                        subtract -= tier.tier_range_high - 1
                        if(subtract < 0):
                            remainder = subtract + tier.tier_range_high - 1 
                            charge = float(tier.billing_amount) * (remainder) 
                            charge_sum += charge
                        else:
                            charge = float(tier.billing_amount) * (tier.tier_range_high - 1)
                            charge_sum += charge
                    else:
                        print("Not subtracting any more")
        charge_without_county = charge_sum
        county_charges = Charge.objects.filter(county=profile.county)
        service_charge = 0
        float(service_charge)
        for charge in county_charges: 
            service_charge += charge.charge_amount
        final_charge = float(service_charge) + charge_sum
        final_charge = round(final_charge, 2)
        return final_charge 

    def bill_user(self, pk): 
        user_profile = self.get_profile(pk=pk)
        final_charge = self.charge_tier_usage(user_profile.pk)
        profile_tier_usage = self.get_property_tier_usage(user_profile.pk) 
        county_charge_total = self.get_county_charge_total(user_profile.pk) 
        create_bill = Bill.objects.create(state=user_profile.state.code, county=user_profile.county.title, tier_water_usage=profile_tier_usage.title, service_charge_total=county_charge_total,total_amount=final_charge, user=user_profile.user)  
        county_charges = Charge.objects.filter(county=user_profile.county)
        for charge in county_charges: 
            create_bill.charges.add(charge)
        create_bill.save() 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = models.CharField(max_length=100) 
    date_posted = models.DateTimeField(default=timezone.now) 
    bio = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    hcf_usage = models.IntegerField()
    user_property = models.ForeignKey(Property, on_delete=models.CASCADE) 
    objects = ProfileManager() 

    class Meta:
        ordering = ['date_posted']  

    def __str__(self):
        return  '{} Profile'.format(self.user.username)



