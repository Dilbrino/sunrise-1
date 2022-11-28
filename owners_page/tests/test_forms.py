from django.test import SimpleTestCase
from owners_page.forms import *


class TestFroms(SimpleTestCase):
    # Write code for Testfrom check Method and Validation working Properly
    def carFormValidData(self):
        form = CarForm(data={
            'car_name': 'City',
            'car_model': 'Y92022',
            'car_seats': '5',
            'gearbox': '2',
            'price': '349999',
            'extra_info': 'Ac',
        })
        self.assertTrue(form.is_valid())

    def customerNoData(self):
        form = CarForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)


class CarEditForm(SimpleTestCase):
    # Write code for Testfrom check Method and Validation working Properly
    def CarEditFormValidData(self):
        form = filter(data={
            'model': 'car',
            'exclude': ['owner', 'available_car', 'date_added']
        })
        self.assertTrue(form.is_valid())

    def CarEditFormNoData(self):
        form = filter(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)


class ownerForm(SimpleTestCase):
    # Write code for Testfrom check Method and Validation working Properly
    def ownerFormValidData(self):
        form = filter(data={
            'username': 'Malik',
            'password': '9875tyu',
            'mobile': '987766',
            'first_name': 'Irii',
            'last_name': 'Malik',
            'email': 'irri@gmil.com',
        })
        self.assertTrue(form.is_valid())

    def ownerFormFormNoData(self):
        form = filter(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
