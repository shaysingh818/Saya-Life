from rest_framework import serializers
import base64
from drf_extra_fields.fields import Base64ImageField
from rest_framework.validators import UniqueValidator
from locations.models import State, County
from django.contrib.auth.models import User




class ViewStatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('title', 'code', 'id')

class CreateStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('title', 'code')


class CreateCountySerializer(serializers.ModelSerializer):

    class Meta:
        model = County
        fields = ('title',)


class ViewCountySerializer(serializers.ModelSerializer):

    class Meta:
        model = County
        fields = ('title', 'id')




