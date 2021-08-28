from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from . import views

import unittest

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/tinyOrganicApp/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tinyOrganicApp/base.html')
    
    def test_home_page_contains_correct_html(self):
        response = self.client.get('/tinyOrganicApp/')
        self.assertContains(response, '<p>Hello Tiny Organics hire your boy for this job, im trying to eat out here!</p>')














# class ApiCallsTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def was_allergens_called(self):
#         response = self.client.get('https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/')

#         self.assertEquals(response.status_code, 200, 'API dont work bruh!')


