from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.CharField(max_length=50)
    description = models.TextField(max_length=500,null=True)
