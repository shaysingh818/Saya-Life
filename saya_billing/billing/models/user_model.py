from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .state_county_model import State, County

class ProfileManager(models.Manager):

    def get_account_id(self, id_request):
        account = self.get(account_id=id_request)
        return account

    def get_hcf_usage(self, pk): 
        account = self.get(pk=pk)
        return account.hcf_usage


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = models.CharField(max_length=100) 
    date_posted = models.DateTimeField(default=timezone.now) 
    bio = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    hcf_usage = models.IntegerField()
    objects = ProfileManager() 

    class Meta:
        ordering = ['date_posted']  

    def __str__(self):
        return  '{} Profile'.format(self.user.username)
