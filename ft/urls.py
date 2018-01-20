##
 # ft/urls.py:
 #
 # St: 2018-01-20 Sat 12:02 PM
 # Up: 2018-01-20 Sat 12:02 PM
 #
 # Author: SPS
 ##

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

