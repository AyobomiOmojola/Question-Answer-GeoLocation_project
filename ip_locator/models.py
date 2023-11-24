from django.db import models
from django.contrib.auth.models import User
from rest_framework_api_key.models import APIKey

# Create your models here.
class location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False, related_name='locate_user')
    state = models.CharField(max_length=264, null=True)

class APIKEYMOD(models.Model):
    api_key = models.ForeignKey(APIKey, on_delete=models.CASCADE, related_name='k_apikey' )
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_apikey')
