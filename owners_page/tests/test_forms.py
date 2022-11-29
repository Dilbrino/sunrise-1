from django.test import SimpleTestCase
from owners_page.forms import *


class TestFroms(SimpleTestCase):
    def carFormValidData(self):
        form = CarForm(data={
            'car_name': 'Toyota',
            'car_model': '1990 ',
            'car_seats': '5',
            'gearbox': 'manual',
            'price': '80',
            'extra_info': 'strong car',
        })
        self.assertTrue(form.is_valid())

    def customerNoData(self):
        form = CarForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)



class ownerForm(SimpleTestCase):
    def ownerFormValidData(self):
        form = filter(data={
            'username': 'rebeca22',
            'password': 'luv123',
            'mobile': '45895623',
            'first_name': 'Rebeca',
            'last_name': 'Peter',
            'email': 'rebeba2@gmil.com',
        })
        self.assertTrue(form.is_valid())

    def ownerFormFormNoData(self):
        form = filter(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
