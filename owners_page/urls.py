"""Defines URL patters for owners_page."""
from django.urls import path, include
from . import views

#owners page
urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('owner_home', views.index, name='owner_home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='register'),
    path('car_added', views.add_car, name='car_added'),
    #path('', views.auth_owner, name='auth_owner')
]

