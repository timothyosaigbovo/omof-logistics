from django.test import TestCase
from django.contrib.auth.models import User
from quotes.models import QuoteRequest, Quote
from .models import Order
import datetime


class OrderModelTest(TestCase):

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

    def test_order_number_generated(self):
        order = Order.objects.create(
            user=self.user,
            quote=self.quote,
            amount_paid=1500.00,
            currency='GBP',
            status='pending'
        )
        self.assertIsNotNone(order.order_number)
        self.assertEqual(len(order.order_number), 32)

    def test_order_str(self):
        order = Order.objects.create(
            user=self.user,
            quote=self.quote,
            amount_paid=1500.00,
            currency='GBP',
            status='pending'
        )
        self.assertIn('GBP', str(order))
