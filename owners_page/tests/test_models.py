from django.test import TestCase
from customer_page.models import *
from customer_page.models import Customer


class TestModel(TestCase):
    # Write code for TestModel check Mdel working Properly
    def setUp(self):
        self.carowner1 = CarOwner.objects.create(
            mobile='47126589',
            location='Bodø'
        )

    def CarOwner(self):
        customer = Customer.objects.create(
            owner=self.customer1,
            wallet=2100

        )
        self.assertEquals(self.carowner1.first_name.first().last_name)


class TestModelCarr(TestCase):
    # Write code for TestModelOrder check Model working Properly
    def setUp(self):
        self.car1 = Car.objects.create(
            car_name='Bobil',
            car_seats='12',
            car_model='Mh89'
        )

        self.assertEquals(self.car1.rent.first().car)
