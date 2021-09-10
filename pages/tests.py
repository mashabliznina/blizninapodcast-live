from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

from .views import HomePageView, ContactPageView, EpisodePageView, EpisodesPagesView

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    
    def test_contacts_page_status_code(self):
        response = self.client.get('/contacts_page/')
        self.assertEqual(response.status_code, 200)

    
    def test_episode_page_status_code(self):
        response = self.client.get('/episode/')
        self.assertEqual(response.status_code, 200)


    def test_episodes_page_status_code(self):
        response = self.client.get('/episodes/')
        self.assertEqual(response.status_code, 200)


