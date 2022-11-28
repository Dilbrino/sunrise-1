from django.test import TestCase
from django.urls import reverse, resolve
from owners_page.views import *
from django.test import SimpleTestCase


# Create your tests here.
# Test Case for Owners_Page App URLS,,,,,,,,,,,,,

class TestUrlsIst(SimpleTestCase):

    def owner_home(self):
        url = reverse('owner_home')
        self.assertEquals(resolve(url).func, index)

    def login(self):
        url = reverse('owner_login')
        self.assertEquals(resolve(url).func, login_view)

    def register(self):
        url = reverse('owner_register')
        self.assertEquals(resolve(url).func, registration)


class TestUrlsTwo(SimpleTestCase):

    def car_added(self):
        url = reverse('car_added')
        self.assertEquals(resolve(url).func, add_car)

    def edit_car(self):
        url = reverse('edit_car')
        self.assertEquals(resolve(url).func, edit_car)

    def delete_car(self):
        url = reverse('delete_car')
        self.assertEquals(resolve(url).func, delete_car)


class TestUrlsThree(SimpleTestCase):

    def manage(self):
        url = reverse('manage')
        self.assertEquals(resolve(url).func, manage)

    def password_change(self):
        url = reverse('password_change')
        self.assertEquals(resolve(url).func, password_change)

    def logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_user)
