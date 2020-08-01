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


