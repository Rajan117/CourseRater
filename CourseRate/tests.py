from django.test import TestCase
import importlib
import os

# Create your tests here.
class HomeViewTests(TestCase):
    """
    Tests the home view
    """

    def setUp(self):
        self.views_module = importlib.import_module('CourseRate.views')
        self.views_module_listing = dir(self.views_module)

        self.project_urls_module = importlib.import_module('CourseRate.urls')

        def test_view_exists(self):

            #Test if the home() view exists in CourseRate views.py views_module

            name_exists = 'home' in self.views_module_listing
            is_callable = callable(self.views_module.index)

            self.assertTrue(name_exists, )

        
