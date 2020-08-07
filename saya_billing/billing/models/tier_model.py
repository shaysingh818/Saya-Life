from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from locations.models import County 

class LotSize(models.Model): 
    title = models.CharField(max_length=100, unique=True)
    lot_size_low = models.IntegerField()
    lot_size_high = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now) 
    county = models.ForeignKey(County, on_delete=models.CASCADE) 

    def __str__(self): 
        return "{}".format(self.title) 


class Tier(models.Model): 
    title = models.CharField(max_length=100, unique=True) 
    tier_range_low = models.IntegerField()
    tier_range_high = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    lot_size = models.ForeignKey(LotSize, on_delete=models.CASCADE)
    billing_amount = models.DecimalField(max_digits=7, decimal_places=2) 


    def __str__(self): 
        return "{}".format(self.title)




