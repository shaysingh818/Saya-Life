from django.shortcuts import render
from billing.models import State, County, LotSize , Tier
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


#Create, Read, Update, Delete Playlist
class StatesView(APIView):
    def get(self, request, format=None):
        states = State.objects.all()
        serializer = ViewStatesSerializer(states, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        context = {"reuquest": request}
        serializer = CreateStateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Message": "Created State"})
        else:
            return Response({"Message": "Failed to create State"})


class StateView(APIView):

    def get_object(self, pk):
        try:
            return State.objects.get(pk=pk)
        except State.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        state = self.get_object(pk)
        serializer = ViewStatesSerializer(state)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        select_state = self.get_object(pk) 
        serializer = CreateCountySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(state=select_state)
            return Response({"Message": "Created County"})
        else:
            return Response({"Message": "Failed to create County"})

    def delete(self, request, pk, format=None):
        state = self.get_object(pk)
        state.delete()
        return Response({"Message": "State was deleted"})


#Create, Read, Update, Delete Playlist
class CountiesView(APIView):
    def get(self, request, format=None):
        counties = County.objects.all()
        serializer = ViewCountySerializer(counties, many=True)
        return Response(serializer.data)

class CountyView(APIView):

    def get_object(self, pk):
        try:
            return County.objects.get(pk=pk)
        except County.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        county = self.get_object(pk)
        serializer = ViewCountySerializer(county)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        state = self.get_object(pk)
        state.delete()
        return Response({"Message": "County was deleted"})


#View Counties Under State
class CountyStateView(APIView):

    def get_object(self, pk):
        try:
            return State.objects.get(pk=pk)
        except State.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        state = self.get_object(pk)
        counties = County.objects.filter(state=state)
        serializer = ViewCountySerializer(counties, many=True)
        return Response(serializer.data)


class LotSizeCounty(APIView):

    def get_object(self, pk):
        try:
            return County.objects.get(pk=pk)
        except County.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        county = self.get_object(pk)
        lot_sizes = LotSize.objects.filter(county=county)
        serializer = ViewLotSerializer(lot_sizes, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        select_county = self.get_object(pk)
        serializer = CreateLotSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(county=select_county)
            return Response({"Message": "Created Lot Size"})
        else:
            return Response({"Message": "Failed to create Lot Size"})



class LotSizeTiers(APIView):

    def get_object(self, pk):
        try:
            return LotSize.objects.get(pk=pk)
        except LotSize.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lot_size = self.get_object(pk)
        tiers = Tier.objects.filter(lot_size=lot_size)
        serializer = ViewTierSerializer(tiers, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        lot_size = self.get_object(pk)
        serializer = CreateTierSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(lot_size=lot_size)
            return Response({"Message": "Created Tier for Lot"})
        else:
            return Response({"Message": "Failed to create tier for lot"})





#Add Lot Sizes County




#Add Tiers for lot Size county







