# tracking/models.py
# Models for shipment tracking — linked to a paid Order.
# Admin creates Shipment records and adds ShipmentUpdate entries
# to build a timeline visible to the customer.

from django.db import models
from checkout.models import Order


class Shipment(models.Model):
    """
    Represents a shipment linked one-to-one with a paid Order.
    Tracks the current status and estimated delivery date.
    Admin creates and manages shipments via the Django admin panel.
    """

    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('collected', 'Collected'),
        ('in_transit', 'In Transit'),
        ('customs', 'Customs Clearance'),
        ('delivered', 'Delivered'),
    ]

    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name='shipment'
    )
    # Unique human-readable tracking reference e.g. OMOF-2026-001
    tracking_reference = models.CharField(max_length=100, unique=True)
    current_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='booked'
    )
    estimated_delivery = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Shipment {self.tracking_reference} "
            f"— {self.get_current_status_display()}"
        )


class ShipmentUpdate(models.Model):
    """
    Represents a single status update on a shipment timeline.
    Multiple updates build the animated tracking timeline shown to the customer.
    Ordered chronologically by timestamp.
    """

    shipment = models.ForeignKey(
        Shipment, on_delete=models.CASCADE, related_name='updates'
    )
    status = models.CharField(max_length=20, choices=Shipment.STATUS_CHOICES)
    # Optional location description e.g. London Heathrow
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return (
            f"{self.shipment.tracking_reference} "
            f"— {self.status} at {self.timestamp:%d %b %Y %H:%M}"
        )
