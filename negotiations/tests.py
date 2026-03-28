from django.test import TestCase
from django.contrib.auth.models import User
from quotes.models import QuoteRequest, Quote
from .models import NegotiationMessage
import datetime


class NegotiationMessageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.rfq = QuoteRequest.objects.create(
            user=self.user,
            origin='London',
            destination='Lagos',
            cargo_description='Electronics',
            urgency='standard'
        )
        self.quote = Quote.objects.create(
            quote_request=self.rfq,
            proposed_price=1500.00,
            currency='GBP',
            valid_until=datetime.date.today(),
            notes='Test quote'
        )

    def test_message_created(self):
        msg = NegotiationMessage.objects.create(
            quote=self.quote,
            sender=self.user,
            message='Can you reduce the price?',
            is_admin=False
        )
        self.assertEqual(msg.message, 'Can you reduce the price?')
        self.assertFalse(msg.is_admin)

    def test_admin_message_flag(self):
        msg = NegotiationMessage.objects.create(
            quote=self.quote,
            sender=self.user,
            message='We can offer a 10% discount.',
            is_admin=True
        )
        self.assertTrue(msg.is_admin)
