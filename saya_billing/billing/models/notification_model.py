from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class NotificationManager(models.Manager):

    def get_notifs(self):
        notifs = self.all()
        return notifs


class Notification(models.Model):
    title = models.CharField(max_length=100) 
    date_posted = models.DateTimeField(default=timezone.now)
    to_user = models.OneToOneField(User, on_delete=models.CASCADE) 

    objects = NotificationManager()

    def __str__(self):
        return 'Notfiication {} to {}'.format(self.title, self.user.username) 
