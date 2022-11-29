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

    def test_registration_user_post(self):
        User.objects.create(
            project=self.user1,
            username='ronaldo10'
        )

        response = self.client.post(self.registration_url, {
            'first_name': 'Umari',
            'last_name': 'Erik',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.first_name.first().last_name, 'Erik')

    def test_registration_user_data(self):
        response = self.client.post(self.registration_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user1.first_name.first().count(), 0)
