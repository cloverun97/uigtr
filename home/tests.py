from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, landing_page_content, mhs_name
from django.http import HttpRequest
from unittest import skip

# Create your tests here.

class HomeUnitTest(TestCase):

    def test_home_url_is_exist(self):
        response = Client().get('/home/')
        self.assertEqual(response.status_code,200)

    def test_home_using_index_func(self):
        found = resolve('/home/')
        self.assertEqual(found.func, index)

