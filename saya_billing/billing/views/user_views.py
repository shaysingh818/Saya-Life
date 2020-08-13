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


class CurrentBill(APIView): 
    def get(self, request): 
        user_request = request.user
        profile = Profile.objects.get(user=user_request)
        charge_sum = Profile.objects.charge_tier_usage(profile.pk)
        tier_usage = Profile.objects.get_property_tier_usage(profile.pk)
        hcf_usage = Profile.objects.get_hcf_usage(profile.pk)
        gallons = Profile.objects.get_hcf_gallons(profile.pk) 
        tier_title = tier_usage.title
        service_charges = Profile.objects.display_county_charges(profile.pk)
        service_total = Profile.objects.get_county_charge_total(profile.pk) 
        return Response({"charge_sum": charge_sum, "tier": tier_title, "HCF": hcf_usage, "gallons": gallons, "service_charges": service_charges, "service_total":service_total}) 


class WaterUsageMeter(APIView): 

    def get_object(self, pk): 
        try: 
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk): 
        user_request = self.get_object(pk) 
        profile = Profile.objects.get(user=user_request)
        hcf_usage = Profile.objects.get_hcf_usage(profile.pk)  
        hcf_gallons = Profile.objects.get_hcf_gallons(profile.pk) 
        return Response({"HCF": hcf_usage, "Gallons": hcf_gallons}) 


