from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from billing.models import Charge
from .tier_model import Tier, LotSize

class County(models.Model): 
    title = models.CharField(max_length=100, unique=True)
    date_posted = models.DateTimeField(default=timezone.now) 
    service_charges = models.ManyToManyField(Charge, related_name='countycharges', blank=True) 
    lot_sizes = models.ManyToManyField(LotSize, related_name='countylots', blank=True)
    tier_ranges = models.ManyToManyField(Tier, related_name='countytiers', blank=True) 

    def __str__(self): 
        return "{}".format(self.title) 

class State(models.Model): 
    title = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=2) 
    date_posted = models.DateTimeField(default=timezone.now) 
    counties = models.ManyToManyField(County, related_name='statecounties', blank=True) 

    def __str__(self): 
        return "{}".format(self.title)



