from django.db import models
from django.contrib.auth.models import User
# from rest_framework_api_key.models import APIKey

# Create your models here.
class location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False, related_name='locate_user')
    state = models.CharField(max_length=264, null=True)

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_profile')
    bio = models.CharField(max_length=264, verbose_name="Write a short bio about yourself", null=True)
    date_of_birth = models.DateField(null = True)


class APIKEYMOD(models.Model):
    api_key = models.CharField(max_length=264, null=True)
    user =  models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='user_apikey')
    api_key_creation_date = models.DateTimeField(auto_now_add=True)
    api_key_expiry_date = models.DateTimeField(null=True)