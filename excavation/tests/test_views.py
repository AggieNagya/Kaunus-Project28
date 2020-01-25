from django.test import TestCase, Client
from excavation.models import *
from django.urls import reverse, resolve


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        response = self.client.post('/accounts/login/', {'username': 'admin21', 'password': '12345'})

        self.assertEquals(response.status_code, 200)

    def test_TrenchListView_GET(self):
        response = self.client.get(reverse('trenches'))
        print("Response is Below")
        print(response)
        print("In this test_TrenchListView_GET")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'excavation/trench_list.html')


