from django.test import TestCase
from django.contrib.auth.models import User
from services.models import ServiceCategory, Service
from .models import QuoteRequest, Quote
import datetime


class QuoteRequestModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123', email='testuser@example.com'
        )
        self.category = ServiceCategory.objects.create(
            name='Freight', slug='freight', description='Freight services'
        )
        self.service = Service.objects.create(
            category=self.category,
            name='Air Freight',
            slug='air-freight',
            description='Fast air freight'
        )

    def test_quoterequest_created(self):
        rfq = QuoteRequest.objects.create(
            user=self.user,
            service=self.service,
            origin='London',
            destination='Lagos',
            cargo_description='Electronics',
            urgency='standard',
            status='pending'
        )
        self.assertIn('Pending', str(rfq))

    def test_quoterequest_default_status(self):
        rfq = QuoteRequest.objects.create(
            user=self.user,
            origin='London',
            destination='Lagos',
            cargo_description='Electronics',
            urgency='standard'
        )
        self.assertEqual(rfq.status, 'pending')


class QuoteModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser2', password='testpass123'
        )
        self.rfq = QuoteRequest.objects.create(
            user=self.user,
            origin='London',
            destination='Lagos',
            cargo_description='Electronics',
            urgency='standard'
        )

    def test_quote_created(self):
        quote = Quote.objects.create(
            quote_request=self.rfq,
            proposed_price=1500.00,
            currency='GBP',
            valid_until=datetime.date.today(),
            notes='Standard rate applies'
        )
        self.assertEqual(quote.currency, 'GBP')
        self.assertEqual(float(quote.proposed_price), 1500.00)
