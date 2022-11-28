from django.test import TestCase
from customer_page.models import *
from customer_page.models import Customer


class TestModel(TestCase):
    # Write code for TestModel check Mdel working Properly
    def setUp(self):
        self.carowner1 = CarOwner.objects.create(
            mobile='9876543',
            location='pakistan'
        )

    def CarOwner(self):
        customer = Customer.objects.create(
            owner=self.customer1,
            wallet=4500

        )
        self.assertEquals(self.carowner1.first_name.first().last_name)


class TestModelCarr(TestCase):
    # Write code for TestModelOrder check Model working Properly
    def setUp(self):
        self.car1 = Car.objects.create(
            car_name='Royll',
            car_seats='8',
            car_model='civic2022'
        )

        self.assertEquals(self.car1.rent.first().car)
