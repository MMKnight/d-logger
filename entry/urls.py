from django.conf.urls import url
from django.urls import reverse
from . import views

app_name = 'entry'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name = 'index'),
    url(r'^new/$',views.NewEntry.as_view(),name= 'new'),
    url(r'^(?P<pk>[0-9]+)/$',views.DisplayEntry.as_view(),name= 'detail'),
]
