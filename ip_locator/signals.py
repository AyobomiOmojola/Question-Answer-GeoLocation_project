# from django.db.models.signals import post_save
# from .models import APIKEYMOD
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Userprofile
# import uuid


# @receiver(post_save, sender=Userprofile)
# def GenerateAPiKey(**kwargs):
#     my_api_key = uuid.uuid4()
#     api_keys = APIKEYMOD(api_key=my_api_key,user=request.user)
#     api_keys.save()

