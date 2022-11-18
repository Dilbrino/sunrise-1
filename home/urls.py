"""Defines URL patters for the home page."""
from django.urls import path, include
from . import views
from owners_page.models import *
from customer_page.models import *

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('', views.home_page, name='home'),

]