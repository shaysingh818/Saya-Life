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

#add charges under county
class AddCharge(APIView): 

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

    def post(self, request, title):
        county = self.get_object(title=title)
        serializer = CreateChargeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(county=county)
            return Response({"Message": "Created Charge"})
        else: 
            return Response({"Message": "Unable to add charge"}) 


class BillView(APIView): 

    def get_object(self, pk): 
        try:
            return Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            raise Http404

    def get(self, request, pk): 
        bill = self.get_object(pk) 
        serializer = ViewBillSerializer(bill) 
        return Response(serializer.data) 

    def put(self, request, pk): 
        bill = self.get_object(pk) 
        serializer = CreateBillSerializer(bill, data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.data) 
            return Response({"Message": "Updated Bill"}) 

    def delete(self, request, pk, format=None):
        bill = self.get_object(pk)
        bill.delete()
        return Response({"Message": "Bill was deleted"})



class BillChargesView(APIView):

    def get_object(self, pk): 
        try:
            return Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bill = self.get_object(pk)
        charges = bill.charges.all()
        serializer = ViewChargeSerializer(charges, many=True)
        return Response(serializer.data) 

class UserProperty(APIView): 

    def get_object(self, pk): 
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk): 
        user = self.get_object(pk)
        profile = Profile.objects.get(user=user)
        user_property = profile.user_property
        serializer = ViewPropertySerializer(user_property) 
        return Response(serializer.data) 

    def put(self, request, pk): 
        user = self.get_object(pk)
        profile = Profile.objects.get(user=user)
        user_property = profile.user_property
        serializer = UpdatePropertySerializer(user_property, data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.data) 
            return Response({"Message": "Updated Bill"}) 
        else: 
            return Response({"Message": "Could not update property info"}) 

class BillUser(APIView):

    def get_object(self, pk): 
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        profile = Profile.objects.get(user=user)
        bill_user = Profile.objects.bill_user(profile.pk)
        return Response({"Message": "Billed user"}) 

#Add lot size for specific county
class ViewBills(APIView):
    def get(self, request, format=None):
        bills = Bill.objects.all()
        serializer = ViewBillSerializer(bills, many=True)
        return Response(serializer.data)
