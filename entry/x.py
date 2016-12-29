from django import forms
from django.contrib.postgres import forms as pg
class Entry(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.TextField(max_length=1300)
    tags = pg.SplitArrayField(models.CharField(max_length=12),size=5)