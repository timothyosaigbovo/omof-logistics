from django.db import models
from django.contrib.auth.models import User
from quotes.models import Quote
import uuid


class Order(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    CURRENCY_CHOICES = [
        ('GBP', 'British Pound'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('NGN', 'Nigerian Naira'),
        ('CAD', 'Canadian Dollar'),
        ('GHS', 'Ghanaian Cedi'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders'
    )
    quote = models.OneToOneField(
        Quote, on_delete=models.CASCADE, related_name='order'
    )
    order_number = models.CharField(max_length=32, unique=True, editable=False)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='GBP')
    stripe_payment_intent_id = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} — {self.currency} {self.amount_paid}"
