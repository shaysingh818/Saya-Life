from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from billing.models import Charge

class LotSize(models.Model): 
    title = models.CharField(max_length=100, unique=True)
    lot_size_low = models.IntegerField()
    lot_size_high = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self): 
        return "{}".format(self.title) 

class Tier(models.Model): 
    title = models.CharField(max_length=100, unique=True) 
    tier_range_low = models.IntegerField()
    tier_range_high = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self): 
        return "{}".format(self.title)

