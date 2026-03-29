# tracking/views.py
# Displays the shipment tracking timeline to the customer.

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shipment


@login_required
def tracking_detail(request, tracking_reference):
    """
    Display the tracking timeline for a shipment.
    Only accessible by the user who placed the order.
    Retrieves all status updates ordered chronologically.
    """
    # Ensure the shipment belongs to the logged-in user via the order
    shipment = get_object_or_404(
        Shipment,
        tracking_reference=tracking_reference,
        order__user=request.user
    )

    # Fetch all timeline updates for this shipment
    updates = shipment.updates.all()

    return render(request, 'tracking/tracking_detail.html', {
        'shipment': shipment,
        'updates': updates,
    })
