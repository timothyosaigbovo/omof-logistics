# quotes/models.py
# Models for the quote request and quote issuance flow.
# Clients submit QuoteRequests; admin responds with a Quote.
# No prices are stored on the Service model — all pricing is via Quote only.

from django.db import models
from django.contrib.auth.models import User
from services.models import Service


class QuoteRequest(models.Model):
    """
    Submitted by a client requesting a custom shipping quote.
    Tracks the full shipment details, urgency and current status.
    Status progresses: pending → quoted → negotiating → accepted/rejected.
    """

    URGENCY_CHOICES = [
        ('standard', 'Standard'),
        ('express', 'Express'),
        ('urgent', 'Urgent'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('quoted', 'Quoted'),
        ('negotiating', 'Negotiating'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='quote_requests'
    )
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='quote_requests'
    )
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    cargo_description = models.TextField()
    estimated_weight_kg = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    urgency = models.CharField(
        max_length=20, choices=URGENCY_CHOICES, default='standard'
    )
    special_requirements = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending'
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"RFQ #{self.pk} — {self.user.email} — {self.get_status_display()}"


class Quote(models.Model):
    """
    Issued by admin in response to a QuoteRequest.
    Linked one-to-one with a QuoteRequest.
    Contains the proposed price, currency, validity and admin notes.
    """

    quote_request = models.OneToOneField(
        QuoteRequest, on_delete=models.CASCADE, related_name='quote'
    )
    proposed_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Currency code e.g. GBP, USD, EUR
    currency = models.CharField(max_length=3, default='GBP')
    valid_until = models.DateField()
    notes = models.TextField(help_text='Explain the pricing to the client')
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Quote for RFQ #{self.quote_request.pk} "
            f"— {self.currency} {self.proposed_price}"
        )
