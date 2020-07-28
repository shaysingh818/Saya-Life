from django.contrib import admin
from billing.models import Notification, Profile, Charge
# Register your models here.

admin.site.register(Notification)
admin.site.register(Profile)
admin.site.register(Charge)
