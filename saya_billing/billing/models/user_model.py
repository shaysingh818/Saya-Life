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
        lot_size = prop.lot_size
        county_lot_ranges = LotSize.objects.filter(county=user_profile.county)
        for lot in county_lot_ranges:
            if lot_size in range(lot.lot_size_low, lot.lot_size_high):
                hcf_tiers = Tier.objects.filter(lot_size=lot)
                for tier in hcf_tiers:
                    if hcf_water in range(tier.tier_range_low, tier.tier_range_high):
                        return tier.title

    def bill_all_properties(self): 
        profiles = self.all() 
        for profile in profiles:
            profile_tier_usage = self.get_property_tier_usage(profile.pk) 
            county_charges = Charge.objects.filter(county=profile.county)
            charge_sum = 0
            for charge in county_charges: 
                charge_sum += charge.charge_amount
        
            print(charge_sum)
            print(profile_tier_usage)

            create_bill = Bill.objects.create(tier_water_usage=profile_tier_usage, service_charge_total=charge_sum,total_amount=1600, user=profile.user)
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



