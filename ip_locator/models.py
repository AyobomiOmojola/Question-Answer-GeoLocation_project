from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False, related_name='locate_user')
    state = models.CharField(max_length=264, null=True)
