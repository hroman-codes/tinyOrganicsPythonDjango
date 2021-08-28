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

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/tinyOrganicApp/')
        self.assertNotContains(response, '<h1>Delete Delete Delete<h1>')

class FormPageTest(SimpleTestCase):
    def test_form_page_status_code(self):
        response = self.client.get('/tinyOrganicApp/form/#container')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('form'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('form'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tinyOrganicApp/form.html')
    
    def test_home_page_contains_correct_html(self):
        response = self.client.get('/tinyOrganicApp/form/#container')
        self.assertContains(response, "<h1>Customer Form 📝</h1>")

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/tinyOrganicApp/form/#container')
        self.assertNotContains(response, '<h1>Delete Delete Delete<h1>')













# class ApiCallsTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def was_allergens_called(self):
#         response = self.client.get('https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/')

#         self.assertEquals(response.status_code, 200, 'API dont work bruh!')


