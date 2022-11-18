"""Defines URL patters for customer_page."""
from django.urls import path
from . import views

urlpatterns = [
    path('customer_home', views.index, name='customer_home'),
    path('login', views.login, name='login-view'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='registration'),

]



