from rest_framework import serializers
import base64
from drf_extra_fields.fields import Base64ImageField
from rest_framework.validators import UniqueValidator
from billing.models import Notification, Profile, Charge, State, County, LotSize, Tier, Property
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ( 'id' , 'username', 'email', 'password')

    def create(self, validated_data):
        user = super(RegistrationSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


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
        fields = ('title',)



class ViewLotSerializer(serializers.ModelSerializer):

    class Meta:
        model = LotSize
        fields = ('title', 'lot_size_low', 'lot_size_high')


class CreateLotSerializer(serializers.ModelSerializer):

    class Meta:
        model = LotSize
        fields = ('title', 'lot_size_low', 'lot_size_high')

