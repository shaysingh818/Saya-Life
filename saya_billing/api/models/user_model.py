from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ProfileManager(models.Manager):

    def get_account_id(self, id_request):
        account = self.get(account_id=id_request)
        return account


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = models.CharField(max_length=100) 
    date_posted = models.DateTimeField(default=timezone.now) 
    bio = models.TextField()
    objects = ProfileManager() 

    class Meta:
        ordering = ['date_posted']  

    def __str__(self):
        return  '{} Profile'.format(self.user.username)
