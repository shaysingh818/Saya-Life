from rest_framework import serializers
import base64
from drf_extra_fields.fields import Base64ImageField
from rest_framework.validators import UniqueValidator
from .models import Notification, Profile, Charge, LotSize, Tier, Property, Bill
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
        fields = ('title', 'tier_range_low', 'tier_range_high', 'billing_amount')



class ViewTierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tier
        fields = ('title', 'tier_range_low', 'tier_range_high', 'billing_amount')



class ViewChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charge
        fields = ('title', 'charge_amount', 'id')


class CreateChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charge
        fields = ('title', 'charge_amount')


class ViewBillSerializer(serializers.ModelSerializer):

    charges = serializers.SlugRelatedField(many=True, read_only=True,  slug_field='title')

    class Meta:
        model = Bill
        fields = ('date_bill_prepared', 'tier_water_usage','service_charge_total','total_amount', 'due_date', 'id', 'charges')



class ViewPropertySerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(many=False, read_only=True,  slug_field='title')
    county = serializers.SlugRelatedField(many=False, read_only=True,  slug_field='title')

    class Meta:
        model = Property
        fields = ('title', 'address', 'zipcode', 'lot_size', 'date_posted', 'hcf_usage', 'state', 'county')


class UpdatePropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ('hcf_usage', )



class ViewNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('title', 'subtitle', 'date_posted', 'id')
