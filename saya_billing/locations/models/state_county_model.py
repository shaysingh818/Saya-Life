from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class State(models.Model): 
    title = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=2) 
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self): 
        return "{}".format(self.title)


class County(models.Model): 
    title = models.CharField(max_length=100, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    state = models.ForeignKey(State, on_delete=models.CASCADE) 

    def __str__(self): 
        return "{}".format(self.title) 




