from django.contrib import admin
from api.models import Profile, Notification, Charge
# Register your models here.

admin.site.register(Profile)
admin.site.register(Notification)  
admin.site.register(Charge)
