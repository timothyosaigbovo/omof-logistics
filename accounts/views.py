# accounts/views.py
# Handles user profile management and the client dashboard.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from quotes.models import QuoteRequest
from checkout.models import Order


@login_required
def profile(request):
    """
    Display and update the user's profile.
    Creates a UserProfile if one does not already exist.
    """
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'accounts/profile.html', {
        'form': form,
        'profile': user_profile,
    })


@login_required
def dashboard(request):
    """
    Display the client dashboard with summary stats and recent activity.
    Shows RFQ count, order count, in-transit shipments and delivered orders.
    """
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Fetch all RFQs and orders for the logged-in user
    rfqs = QuoteRequest.objects.filter(user=request.user).order_by('-submitted_at')
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # Filter orders that are paid and shipment is not yet delivered
    in_transit = orders.filter(
        status='paid',
        quote__quote_request__status='accepted'
    ).exclude(shipment__current_status='delivered')

    # Filter orders where shipment has been delivered
    delivered = orders.filter(shipment__current_status='delivered')

    return render(request, 'accounts/dashboard.html', {
        'profile': user_profile,
        'rfqs': rfqs,
        'orders': orders,
        'rfq_count': rfqs.count(),
        'order_count': orders.count(),
        'in_transit_count': in_transit.count(),
        'delivered_count': delivered.count(),
    })
