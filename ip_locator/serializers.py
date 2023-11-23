from rest_framework import serializers
from .models import  location

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