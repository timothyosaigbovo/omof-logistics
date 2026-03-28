from django.test import TestCase, Client
from django.urls import reverse
from .models import ContactMessage


class ContactFormTest(TestCase):

    def test_contact_page_loads(self):
        client = Client()
        response = client.get(reverse('contact:contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_form_submission(self):
        client = Client()
        response = client.post(reverse('contact:contact'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test enquiry',
            'message': 'This is a test message'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_message_str(self):
        msg = ContactMessage.objects.create(
            name='Test User',
            email='test@example.com',
            subject='Test enquiry',
            message='Test message'
        )
        self.assertIn('Test User', str(msg))
