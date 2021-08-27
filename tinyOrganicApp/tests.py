from django.test import TestCase
from django.test import SimpleTestCase
from . import views

import unittest

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/tinyOrganicApp/')
        self.assertEquals(response.status_code, 200)


# class ApiCallsTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def was_allergens_called(self):
#         response = self.client.get('https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/')

#         self.assertEquals(response.status_code, 200, 'API dont work bruh!')


