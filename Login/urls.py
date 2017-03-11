from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from Login.views import home, delete, edit_item, add_quantity

# We are adding a URL called /home
urlpatterns = [
url(r'^list/$', home, name='items'),
url(r'^delete_item/(?P<pk>\d+)/$', delete, name='delete_item'),
url(r'^edit_item/(?P<id>\d+)/$', edit_item,name='edit_item'),
url(r'^add_quantity/(?P<id>\d+)/$', add_quantity,name='add_quantity'),
]
