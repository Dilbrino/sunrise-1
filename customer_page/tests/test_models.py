from django.test import TestCase
from customer_page.models import *
from customer_page.models import Customer


class TestModel(TestCase):
    # Write code for TestModel check Mdel working Properly
    def setUp(self):
        self.customer1 = Customer.objects.create(
            mobile='9876543',
            location='pakistan'
        )

    def Customer(self):
        customer = Customer.objects.create(
            customer=self.customer1,
            email='umer@gmail.com'

        )
        self.assertEquals(self.user1.first_name.first().last_name)


class TestModelOrder(TestCase):
    # Write code for TestModelOrder check Model working Properly
    def setUp(self):
        self.order1 = Orders.objects.create(
            car_owner='rizwan',
            rent='45000',
            car='civic'
        )

    def Order(self):
        order = Orders.objects.create(
            customer=self.order1,
            days='3'

        )
        self.assertEquals(self.order1.rent.first().car)
