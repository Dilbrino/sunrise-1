"""Defines URL patters for owners_page."""
from django.urls import path, include
from . import views

#owners page
urlpatterns = [
    path('owners_page/owner_home', views.index, name='owner_home'),
    path('owners_page/login', views.login_view, name='owner_login'),
    path('owners_page/logout', views.logout_user, name='owner_logout'),
    path('owners_page/register', views.registration, name='owner_register'),
    path('owners_page/car_added', views.add_car, name='car_added'),
    path('owners_page/edit_car/<id>', views.edit_car, name='edit_car'),
    path('owners_page/delete_car/<id>', views.delete_car, name='delete_car'),
    path('owners_page/manage', views.manage, name='manage'),
    path("owners_page/password_change", views.password_change, name="owner_password_change"),
    #path('', views.auth_owner, name='auth_owner')
]

