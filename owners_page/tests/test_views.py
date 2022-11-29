from django.test import TestCase, Client
from django.urls import reverse
from customer_page.models import *
import json


class TestViewIndex(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('customer_home')
        self.registration_url = reverse('customer_register')
        self.user1 = User.objects.create(
            username='umer malik',
            password='mali@007'
        )

    def test_user_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_page/login.html')

    def test_registration(self):
        response = self.client.get(self.registration_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_page/register.html')



    def test_registration_user_post(self):
        User.objects.create(
            username='rebeca22',
            user=self.user1
        )

        response = self.client.post(self.registration_url, {
            'first_name': 'Rebeca',
            'last_name': 'Peter',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.first_name.first().last_name, 'Peter')

    def test_registration_user_data(self):
        response = self.client.post(self.registration_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.first_name.first().count(), 0)


class add_car(TestCase):

    def setUp(self):
        self.client = Client()
        self.add_car_url = reverse('car_added')
        self.addcar1 = add_car.objects.create(
            car_name='Toya',
            car_model='1990'
        )

    def add_car_GET(self):
        response = self.client.get(self.add_car_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'owners_page/car_added.html')

    def add_car_info(self):
        response = self.client.get(self.add_car_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'owners_page/car_added.html')

    def add_car_post(self):
        add_car.objects.create(
            car_name=self.add_car_url,
            car_model='1990'
        )

        response = self.client.post(self.add_car_url, {
            'first_name': 'Rebeca',
            'last_name': 'Peter',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.first_name.first().last_name, 'rebeca')

    def add_car_data(self):
        response = self.client.post(self.add_car_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.first_name.first().count(), 0)