from django.shortcuts import render,redirect
from django.views import generic
from .models import Entry
# TODO: Add form and user auth
# Create your views here.
class IndexView(generic.ListView):
    context_object_name = 'entries'
    model = Entry
    template_name = 'entry/index.html'
class DisplayEntry(generic.DetailView):
    model = Entry
    template_name = 'entry/detail.html'
class NewEntry(generic.CreateView):
    model = Entry
    fields =['title','content','tags']
    template_name = 'entry/entry_form.html'
