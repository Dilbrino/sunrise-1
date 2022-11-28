from django.test import TestCase, Client
from django.urls import reverse
from customer_page.models import *
import json


class TestViewIndex(TestCase):
    # Write code for TestView check Get Method working Properly
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

    # Write code for TestView check Post Method working Properly

    def test_registration_post(self):
        User.objects.create(
            project=self.user1,
            username='awii malik'
        )

        response = self.client.post(self.registration_url, {
            'first_name': 'Awaa malik',
            'last_name': 'Awaa malik',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.first_name.first().last_name, 'Awa malik')

    def test_registration_post_np_data(self):
        response = self.client.post(self.registration_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.first_name.first().count(), 0)


class add_car(TestCase):
    # Write code for TestView check Get Method working Properly
    def setUp(self):
        self.client = Client()
        self.add_car_url = reverse('car_added')
        self.addcar1 = add_car.objects.create(
            car_name='Civic',
            car_model='UY007'
        )

    def add_car_GET(self):
        response = self.client.get(self.add_car_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'owners_page/car_added.html')

    def add_car_registration(self):
        response = self.client.get(self.add_car_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'owners_page/car_added.html')

    # Write code for TestView check Post Method working Properly

    def add_car_post(self):
        add_car.objects.create(
            project=self.add_car_url,
            model='YU766'
        )

        response = self.client.post(self.add_car_url, {
            'first_name': 'Awaa malik',
            'last_name': 'Awaa malik',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.first_name.first().last_name, 'Awa malik')

    def add_car_data(self):
        response = self.client.post(self.add_car_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.first_name.first().count(), 0)