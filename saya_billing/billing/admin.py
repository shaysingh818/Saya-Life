from django.contrib import admin
from billing.models import Notification, Profile, Charge, State, County, LotSize, Tier, Property
# Register your models here.

admin.site.register(Notification)
admin.site.register(Profile)
admin.site.register(Charge)
admin.site.register(State)
admin.site.register(County)
admin.site.register(LotSize)
admin.site.register(Tier)
admin.site.register(Property)

