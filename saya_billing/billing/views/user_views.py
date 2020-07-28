from django.shortcuts import render
from api.models import *
from api.serializers import *
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
