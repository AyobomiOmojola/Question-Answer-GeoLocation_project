from django.shortcuts import render
import requests
from .models import location
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import APIView 
from .serializers import LocationSerializer
from ipware import get_client_ip



# Create your views here.
class locator(APIView):
    def get(self, request:Request):
        ip = get_client_ip(request)
        print(ip)
        url = f'https://api.ipstack.com/{" "}?access_key=596f72325f924335772dab8008d6803f'
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

# def locator(request):
#     url = f'https://api.ipstack.com/check?access_key=596f72325f924335772dab8008d6803f'
#     response = requests.get(url)
#     data = response.json()
#     city = data.get("city", {})




