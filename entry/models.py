from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1300)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tags')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('entry:detail',args=(self.pk,))
class Tags(models.Model):
    label = models.CharField(max_length=20)
