from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from datetime import datetime

# Create your tests here.

from blogpost.views import index, view_post
from blogpost.models import Blogpost

class HomePageTest(TestCase):
	"""docstring for HomePageTest"""
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, index)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = index(request)
		self.assertIn(b'<title>Welcome to my blog</title>',response.content)

	def test_blogpost_create_with_show_in_homepage(self):
		Blogpost.objects.create(title='hello', author='admin', slug='this_is_a_test', body='this is a blog',
			posted=datetime.now)
		response = self.client.get('/')
		#request = HttpRequest()
		#response = index(request)
		self.assertIn(b'this is a blog',response.content)


class BlogpostTest(TestCase):
	"""docstring for BlogpostTest"""
	def test_blogpost_url_resolves_to_blog_post_view(self):
		Blogpost.objects.create(title='hello', author='admin', slug='this_is_a_test', body='this is a blog',
			posted=datetime.now)
		found = resolve('/blog/this_is_a_test.html')
		self.assertEqual(found.func, view_post)
		