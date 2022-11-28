from django.test import SimpleTestCase
from customer_page.forms import *


class TestFroms(SimpleTestCase):
    # Write code for Testfrom check Method and Validation working Properly
    def customerValidData(self):
        form = customerForm(data={
            'username': 'ali',
            'password': 'ali876',
            'mobile': '98765',
            'location': 'pakki',
            'first_name': 'ali',
            'last_name': 'malik',
            'email': 'ali@gmail.com'
        })
        self.assertTrue(form.is_valid())

    def customerNoData(self):
        form = customerForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)


class TestFromsFilter(SimpleTestCase):
    # Write code for Testfrom check Method and Validation working Properly
    def filterValidData(self):
        form = filter(data={
            'name': 'ali',
            'model': 'civic',
            'seats': 4,
            'gearBox': '4',
            'location': 'USA',
        })
        self.assertTrue(form.is_valid())

    def filterNoData(self):
        form = filter(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
