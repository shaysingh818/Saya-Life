from django.shortcuts import render
from locations.models import State, County
from billing.models import Tier, LotSize
from billing.serializers import *
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from rest_framework.response import Response
import json
import os
import urllib.request
from rest_framework import generics
from rest_framework import filters
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token


#Add lot size for specific county
class LotSizeCounty(APIView):

    def get_object(self, title):
        try:
            return County.objects.get(title=title)
        except County.DoesNotExist:
            raise Http404

    def get(self, request, title, format=None):
        county = self.get_object(title)
        lot_sizes = LotSize.objects.filter(county=county)
        serializer = ViewLotSerializer(lot_sizes, many=True)
        return Response(serializer.data)

    def post(self, request, title, format=None):
        select_county = self.get_object(title)
        serializer = CreateLotSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(county=select_county)
            return Response(serializer.data)
        else:
            return Response({"Message": "Failed to create Lot Size"})


#Add tier requirements for lot size
class LotSizeTiers(APIView):

    def get_object(self, title):
        try:
            return LotSize.objects.get(title=title)
        except LotSize.DoesNotExist:
            raise Http404

    def get(self, request, title, format=None):
        lot_size = self.get_object(title)
        tiers = Tier.objects.filter(lot_size=lot_size)
        serializer = ViewTierSerializer(tiers, many=True)
        return Response(serializer.data)

    def post(self, request, title, format=None):
        lot_size = self.get_object(title)
        serializer = CreateTierSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(lot_size=lot_size)
            return Response({"Message": "Created Tier for Lot"})
        else:
            return Response({"Message": "Failed to create tier for lot"})


#Add tier requirements for lot size
class CountyCharges(APIView):

    def get_object(self, title):
        try:
            return County.objects.get(title=title)
        except County.DoesNotExist:
            raise Http404

    def get(self, request, title): 
        county = self.get_object(title) 
        charges = Charge.objects.filter(county=county)
        serializer = ViewChargeSerializer(charges, many=True) 
        return Response(serializer.data) 


    def post(self, request, title, format=None):
        county = self.get_object(title)
        serializer = CreateChargeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(county=county)
            return Response({"Message": "Created Charge under county"})
        else:
            return Response({"Message": "Failed to create charge for county"})

    def delete(self, request, title, format=None):
        county = self.get_object(title)
        charge = Charge.objects.get(county=county)
        charge.delete()
        return Response({"Message": "Charge was deleted"})
