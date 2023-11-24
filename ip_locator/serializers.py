from rest_framework import serializers
from .models import  location, APIKEYMOD

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = location
        fields = ['user','state']
        extra_kwargs = {
        "state" : {
            "read_only" : True,
        },
        "user" : {
            "read_only" : True,
        },
    }

class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKEYMOD
        fields = ['user','api_key']
        extra_kwargs = {
        "api_key" : {
            "read_only" : True,
        },
        "user" : {
            "read_only" : True,
        },
    }