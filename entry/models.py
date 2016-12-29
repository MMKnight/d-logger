from django.db import models
from django.urls import reverse
import  django.contrib.postgres.fields as postgres
from django.contrib.auth.models import User
# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1300)
    tags = postgres.ArrayField(models.CharField(max_length=12),size=5,null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('entry:detail',args=(self.pk,))
