from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .state_county_model import State, County
from .tier_model import LotSize, Tier


class Property(models.Model): 
    title = models.CharField(max_length=100) 
    address = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    lot_size = models.IntegerField() 
    date_posted = models.DateTimeField(default=timezone.now) 
    hcf_usage = models.IntegerField() 

    class Meta: 
        ordering = ['date_posted'] 

    def __str__(self): 
        return 'Property {}'.format(self.title) 


class ProfileManager(models.Manager):

    def get_account_id(self, id_request):
        account = self.get(account_id=id_request)
        return account

    def get_hcf_usage(self, pk): 
        account = self.get(pk=pk)
        return account.hcf_usage

    def get_user_properties(self, pk): 
        user_profile = self.get(pk=pk)
        user_properties = user_profile.properties.all()
        return user_properties 

    def get_user_bill(self, pk): 
        user_props = self.get_user_properties(pk)
        user_profile = self.get(pk=pk) 
        #loop thru each user property and generate a bill for each
        for prop in user_props:
            hcf_water = prop.hcf_usage
            lot_size = prop.lot_size
            county_lot_ranges = LotSize.objects.filter(county=user_profile.county)
            for lot in county_lot_ranges: 
                if lot_size in range(lot.lot_size_low, lot.lot_size_high):
                    print(lot) #this is the tier rating we go off
                    #now we go through all the tiers for this lot size
                    hcf_tiers = Tier.objects.filter(lot_size=lot)
                    for tier in hcf_tiers: 
                        if hcf_water in range(tier.tier_range_low, tier.tier_range_high):
                            print(tier) 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = models.CharField(max_length=100) 
    date_posted = models.DateTimeField(default=timezone.now) 
    bio = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    hcf_usage = models.IntegerField()
    properties = models.ManyToManyField(Property, related_name='properties', blank=True) 
    objects = ProfileManager() 

    class Meta:
        ordering = ['date_posted']  

    def __str__(self):
        return  '{} Profile'.format(self.user.username)



