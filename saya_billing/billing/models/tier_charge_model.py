from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from locations.models import State, County

class Charge(models.Model):
    title = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.CASCADE) 
    charge_amount = models.IntegerField()

    def __str__(self): 
        return 'Charge {}'.format(self.title) 


class Bill(models.Model): 
    date_bill_prepared = models.DateTimeField(default=timezone.now)
    tier_water_usage = models.CharField(max_length=100) 
    service_charge_total = models.IntegerField()
    total_amount = models.IntegerField() 
    due_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    charges = models.ManyToManyField(Charge, blank=True, related_name='charges') 

    def __str__(self): 
        return 'Bill for {}'.format(self.user.username) 



