from django.shortcuts import render
import requests
from .models import location, APIKEYMOD
from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import APIView 
from .serializers import LocationSerializer, APIKeySerializer
from ipware import get_client_ip
from dotenv import load_dotenv
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey
import os

load_dotenv()


ACCESS_KEY = os.environ['ACCESS_KEY']
# Create your views here.
class locator(APIView):
    # permission_classes = [HasAPIKey,]
    def get(self, request:Request):
        ip = get_client_ip(request)
        url = f'https://api.ipstack.com/{ip}?access_key={ACCESS_KEY}'
        response = requests.get(url)
        data = response.json()
        city = data.get("city")
        state = location(state=city, user=self.request.user)
        state.save()
        exact_state = location.objects.filter(user=self.request.user)
        serializer = LocationSerializer(instance = exact_state, many=True)

        response = {
            "MESSAGE":"This is the state you are viewing from",
            "YOUR_STATE": serializer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)


class GetAPiKey(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request:Request):
        api_key = APIKEYMOD.objects.get(user = self.request.user)
        serializer = APIKeySerializer(instance=api_key)

        response = {
            "MESSAGE": "THIS IS YOUR API KEY",
            "APIKEY": serializer.data
        }
        return Response(data = response, status = status.HTTP_200_OK)



# def locator(request):
#     url = f'https://api.ipstack.com/check?access_key=596f72325f924335772dab8008d6803f'
#     response = requests.get(url)
#     data = response.json()
#     city = data.get("city", {})




