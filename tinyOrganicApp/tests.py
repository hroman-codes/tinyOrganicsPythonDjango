from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from . import views
from .forms import CustomerForm

import unittest

# Create a user to test DB injection on HTTP Post 

class TestAPI(SimpleTestCase):
    def test_get_api_from_json(self):
        resp = self.api_client.get('http://localhost:8000/api/whatever/?format=json/api/v1/recipes/', format='json')
        self.assertValidJSONResponse(resp)


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
    
    def test_form_page_contains_correct_html(self):
        response = self.client.get('/tinyOrganicApp/form/#container')
        self.assertContains(response, "<h1>Customer Form 📝</h1>")

    def test_form_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/tinyOrganicApp/form/#container')
        self.assertNotContains(response, '<h1>Delete Delete Delete<h1>')
    
    def test_empty_form(self):
        form = CustomerForm()
        self.assertIn("First_Name", form.fields)
        self.assertIn("Last_Name", form.fields)
        self.assertIn("Email", form.fields)
        self.assertIn("Child_First_Name", form.fields)
        self.assertIn("Child_Last_Name", form.fields)
        self.assertIn("Any_Allergies", form.fields)

    def test_form_has_valid_data(self):
        form = CustomerForm(data={
            'First_Name': 'Heriberto',
            'Last_Name': 'Roman',
            'Email': 'builtbygetroman@gmail.com',
            'Child_First_Name': 'Elijah',
            'Child_Last_Name': 'Roman',
            'Any_Allergies': ['shellfish']
        })

        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = CustomerForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)








