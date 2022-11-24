"""Defines URL patters for customer_page."""
from django.urls import path, include
from . import views

urlpatterns = [
    path('customer_page/customer_home', views.index, name='customer_home'),
    path('customer_page/login', views.login, name='customer_login'),
    path('customer_page/register', views.registration, name='customer_register'),
    path('customer_page/manage', views.manage, name='customer_manage'),
    path('customer_page/logout', views.logout_user, name='customer_logout'),
    path('customer_page/rent_car/<id>', views.rent_car, name='rent_car'),
    path('customer_page/giveBack_car/<id>', views.giveBack_car, name='giveBack_car'),
    path("customer_page/password_change", views.password_change, name="password_change"),
    path("customer_page/search_car", views.search_car, name="search_car"),
]
