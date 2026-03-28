from django.db import models
from checkout.models import Order


class Shipment(models.Model):

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
    tracking_reference = models.CharField(max_length=100, unique=True)
    current_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='booked'
    )
    estimated_delivery = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shipment {self.tracking_reference} — {self.get_current_status_display()}"


class ShipmentUpdate(models.Model):
    shipment = models.ForeignKey(
        Shipment, on_delete=models.CASCADE, related_name='updates'
    )
    status = models.CharField(max_length=20, choices=Shipment.STATUS_CHOICES)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.shipment.tracking_reference} — {self.status} at {self.timestamp:%d %b %Y %H:%M}"
