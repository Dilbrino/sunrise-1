from django.test import TestCase
from django.urls import reverse, resolve
from customer_page.views import *
from django.test import SimpleTestCase


# Create your tests here.
# Test Case for Customer_Page App URLS,,,,,,,,,,,,,

class TestUrlsIst(SimpleTestCase):

    def home(self):
        url = reverse('customer_home')
        self.assertEquals(resolve(url).func, index)

    def login(self):
        url = reverse('customer_login')
        self.assertEquals(resolve(url).func, login)

    def register(self):
        url = reverse('customer_register')
        self.assertEquals(resolve(url).func, registration)


class TestUrlsTwo(SimpleTestCase):

    def manage(self):
        url = reverse('customer_manage')
        self.assertEquals(resolve(url).func, manage)

    def logout(self):
        url = reverse('customer_logout')
        self.assertEquals(resolve(url).func, logout_user)

    def rent_car(self):
        url = reverse('rent_car')
        self.assertEquals(resolve(url).func, rent_car)


class TestUrlsThree(SimpleTestCase):

    def GiveBack_car(self):
        url = reverse('giveBack_car')
        self.assertEquals(resolve(url).func, giveBack_car)

    def password_change(self):
        url = reverse('password_change')
        self.assertEquals(resolve(url).func, password_change)

    def search_car(self):
        url = reverse('search_car')
        self.assertEquals(resolve(url).func, search_car)
