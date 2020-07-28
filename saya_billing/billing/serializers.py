from rest_framework import serializers
import base64
from drf_extra_fields.fields import Base64ImageField
from rest_framework.validators import UniqueValidator
from billing.models import Profile, Notification
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

