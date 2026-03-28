from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shipment


@login_required
def tracking_detail(request, tracking_reference):
    shipment = get_object_or_404(
        Shipment,
        tracking_reference=tracking_reference,
        order__user=request.user
    )
    updates = shipment.updates.all()
    return render(request, 'tracking/tracking_detail.html', {
        'shipment': shipment,
        'updates': updates,
    })
