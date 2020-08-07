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
        print("HCF Water usage {}".format(hcf_water))
        charge_sum = 0
        for lot in county_lot_ranges:
            if lot_size in range(lot.lot_size_low, lot.lot_size_high):
                hcf_tiers = Tier.objects.filter(lot_size=lot)
                subtract = hcf_water
                for tier in hcf_tiers:
                    if(subtract > 0):
                        print("{} - {} ".format(subtract, tier.tier_range_high - 1)) 
                        subtract -= tier.tier_range_high - 1
                        print("Subtract value: {}".format(subtract))
                        if(subtract < 0):
                            print("Value {}".format(subtract + tier.tier_range_high - 1))
                            remainder = subtract + tier.tier_range_high - 1 
                            charge = float(tier.billing_amount) * (remainder) 
                            charge_sum += charge
                            print("Final Charge {}".format(charge_sum))
                        else:
                            charge = float(tier.billing_amount) * (tier.tier_range_high - 1)
                            print("{} x {}".format(tier.billing_amount, tier.tier_range_high - 1))
                            print("Charge {} Dollars: ".format(charge))
                            charge_sum += charge
                            #check if value is negative and charge the differnce between 0
                            #if(subtract < 0):
                                #print("Value {}".format(subtract + tier.tier_range_high - 1))
                            print("This the total: {}".format(charge_sum))
                    else:
                        print("Not subtracting any more")

        return "Total Charge {} ".format(charge_sum) 
                   


    def bill_all_properties(self): 
        profiles = self.all() 
        for profile in profiles:
            profile_tier_usage = self.get_property_tier_usage(profile.pk) 
            county_charges = Charge.objects.filter(county=profile.county)
            charge_sum = 0
            for charge in county_charges: 
                charge_sum += charge.charge_amount
            total_billing_amount = profile_tier_usage.billing_amount + charge_sum
            create_bill = Bill.objects.create(state=profile.state.code, county=profile.county.title,tier_water_usage=profile_tier_usage.title, service_charge_total=charge_sum, total_amount=total_billing_amount, user=profile.user)
            for charge in county_charges: 
                create_bill.charges.add(charge) 
            create_bill.save()


    def bill_by_county(self, county): 
        profiles = self.filter(county=county) 
        for profile in profiles:
            profile_tier_usage = self.get_property_tier_usage(profile.pk) 
            county_charges = Charge.objects.filter(county=profile.county)
            charge_sum = 0
            for charge in county_charges: 
                charge_sum += charge.charge_amount
            total_billing_amount = profile_tier_usage.billing_amount + charge_sum
            create_bill = Bill.objects.create(tier_water_usage=profile_tier_usage.title, service_charge_total=charge_sum,total_amount=total_billing_amount, user=profile.user)
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



