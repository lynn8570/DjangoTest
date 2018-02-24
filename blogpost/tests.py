from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.

from blogpost.views import index, view_post

class HomePageTest(TestCase):
	"""docstring for HomePageTest"""
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, index)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = index(request)
		self.assertIn(b'<title>Welcome to my blog</title>',response.content)
