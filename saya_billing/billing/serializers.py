from rest_framework import serializers
import base64
from drf_extra_fields.fields import Base64ImageField
from rest_framework.validators import UniqueValidator
from .models import Notification, Profile, Charge, LotSize, Tier, Property
from django.contrib.auth.models import User



class ViewLotSerializer(serializers.ModelSerializer):

    class Meta:
        model = LotSize
        fields = ('title', 'lot_size_low', 'lot_size_high', 'id')


class CreateLotSerializer(serializers.ModelSerializer):

    class Meta:
        model = LotSize
        fields = ('title', 'lot_size_low', 'lot_size_high')


class CreateTierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tier
        fields = ('title', 'tier_range_low', 'tier_range_high')



class ViewTierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tier
        fields = ('title', 'tier_range_low', 'tier_range_high')



class ViewChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charge
        fields = ('title', 'charge_amount', 'id')


class CreateChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charge
        fields = ('title', 'charge_amount')
