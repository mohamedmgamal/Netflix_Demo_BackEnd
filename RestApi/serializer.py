from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from RestApi import models
from RestApi.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields="__all__"
    def save(self,**kwargs):
        print()
        user = User(
            username = self.validated_data.get('username'),
            first_name =self.validated_data.get('first_name'),
            last_name = self.validated_data.get('last_name'),
             email=self.validated_data.get('email'),
            Address=self.validated_data.get('Address'),
            PhoneNumber=self.validated_data.get("PhoneNumber"),
            cdNumber=self.validated_data.get("cdNumber"),
            cdDate=self.validated_data.get("cdDate"),
            cdName=self.validated_data.get("cdName"),
            password=make_password(self.validated_data.get('password'))
        )
        user.save()
