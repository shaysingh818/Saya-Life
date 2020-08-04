from django.shortcuts import render
from billing.models import *
from billing.serializers import *
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from rest_framework.response import Response
import json
import requests
from rest_framework import generics
from rest_framework import filters
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

#register user to the platform
@permission_classes((AllowAny,))
class RegisterView(APIView):

    def get(self, request):
        return Response({"message": "This view works"})

    def post(self, request):
        if request.method == "POST":
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                if user:
                    token = Token.objects.create(user=user)
                    json = serializer.data
                    return Response(json)

#Get user tier usage for user
class UserWaterUsage(APIView): 

    def get_object(self, pk): 
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist: 
            raise Http404

    def get(self, request, pk):

        user_request = self.get_object(pk) 
        profile = Profile.objects.get(user=user_request)
        hcf_water = profile.user_property.hcf_usage
        lot_size = profile.user_property.lot_size
        gallons = hcf_water * 748

        #get county lot table column
        county_lot_ranges = LotSize.objects.filter(county=profile.county) 
        for lot in county_lot_ranges: 
            if lot_size in range(lot.lot_size_low, lot.lot_size_high):
                hcf_tiers = Tier.objects.filter(lot_size=lot) 
                for tier in hcf_tiers: 
                    if hcf_water in range(tier.tier_range_low, tier.tier_range_high):
                        water_tier_usage = tier.title

        return Response({"HCF" : hcf_water, "Gallons": gallons, "Water Tier Usage": water_tier_usage})


class CurrentBill(APIView): 

    def get_object(self, pk): 
        try: 
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk): 

        user_request = self.get_object(pk) 
        profile = Profile.objects.get(user=user_request)

        user_prop = profile.user_property
        hcf_water_usage = user_prop.hcf_usage
        lot_size = user_prop.lot_size

        county_lot_ranges = LotSize.objects.filter(county=profile.county)
        for lot in county_lot_ranges:
            if lot_size in range(lot.lot_size_low, lot.lot_size_high):
                hcf_tiers = Tier.objects.filter(lot_size=lot)
                for tier in hcf_tiers:
                    if hcf_water_usage in range(tier.tier_range_low, tier.tier_range_high):
                        user_tier = tier

        county_charges = Charge.objects.filter(county=profile.county)
        charge_sum = 0
        for charge in county_charges: 
            charge_sum += charge.charge_amount
        total_billing_amount = user_tier.billing_amount + charge_sum
        
        return Response({"Total": total_billing_amount, "Service_charges": charge_sum, "Water": user_tier.billing_amount, "Water-level": user_tier.title, "Property-size": str(lot_size) + " Square Ft"}) 



