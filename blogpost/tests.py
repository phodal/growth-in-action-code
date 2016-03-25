from datetime import datetime

from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from blogpost.models import Blogpost
from blogpost.views import index, view_post


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertIn(b'<title>Welcome to my blog</title>', response.content)

class BlogpostTest(TestCase):
    def test_blogpost_url_resolves_to_home_page_view(self):
        found = resolve('/blog/this_is_a_test.html')
        self.assertEqual(found.func, view_post)
