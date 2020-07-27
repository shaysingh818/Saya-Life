from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Charge(models.Model):
    title = models.CharField(max_length=100) 

    def __str__(self): 
        return 'Charge {}'.format(self.title) 


