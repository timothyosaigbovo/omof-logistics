from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )

    def test_profile_created_on_user_creation(self):
        profile = UserProfile.objects.get(user=self.user)
        self.assertIsNotNone(profile)

    def test_profile_default_currency(self):
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.preferred_currency, 'GBP')

    def test_dashboard_requires_login(self):
        client = Client()
        response = client.get('/my-account/dashboard/')
        self.assertEqual(response.status_code, 302)

    def test_dashboard_loads_for_logged_in_user(self):
        client = Client()
        client.login(username='testuser', password='testpass123')
        response = client.get('/my-account/dashboard/')
        self.assertEqual(response.status_code, 200)
