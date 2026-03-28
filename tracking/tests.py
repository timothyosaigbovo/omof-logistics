from django.test import TestCase
from django.contrib.auth.models import User
from quotes.models import QuoteRequest, Quote
from checkout.models import Order
from .models import Shipment, ShipmentUpdate
import datetime


class ShipmentTest(TestCase):

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
        self.order = Order.objects.create(
            user=self.user,
            quote=self.quote,
            amount_paid=1500.00,
            currency='GBP',
            status='paid'
        )

    def test_shipment_created(self):
        shipment = Shipment.objects.create(
            order=self.order,
            tracking_reference='OMOF-TEST-001',
            current_status='booked'
        )
        self.assertEqual(shipment.tracking_reference, 'OMOF-TEST-001')
        self.assertEqual(shipment.current_status, 'booked')

    def test_shipment_update_created(self):
        shipment = Shipment.objects.create(
            order=self.order,
            tracking_reference='OMOF-TEST-002',
            current_status='in_transit'
        )
        update = ShipmentUpdate.objects.create(
            shipment=shipment,
            status='in_transit',
            location='Heathrow Airport',
            description='Shipment departed UK'
        )
        self.assertEqual(update.location, 'Heathrow Airport')
