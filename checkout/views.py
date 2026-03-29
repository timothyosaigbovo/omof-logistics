# checkout/views.py
# Handles the booking summary, Stripe checkout and payment success flow.

import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from quotes.models import Quote
from .models import Order
from .forms import CurrencyForm

# Initialise Stripe with the secret key from settings
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def booking_summary(request, quote_pk):
    """
    Display the booking summary page with shipment details and currency selector.
    Only accessible by the quote owner after the quote has been accepted.
    """
    quote = get_object_or_404(Quote, pk=quote_pk)
    rfq = quote.quote_request

    # Ensure only the RFQ owner can access this page
    if rfq.user != request.user:
        messages.error(request, 'You do not have permission to view this.')
        return redirect('quotes:rfq_list')

    # Quote must be accepted before proceeding to payment
    if rfq.status != 'accepted':
        messages.error(request, 'This quote has not been accepted yet.')
        return redirect('negotiations:thread', quote_pk=quote.pk)

    # Pre-fill currency from user profile preference
    currency_form = CurrencyForm(initial={
        'currency': request.user.userprofile.preferred_currency
    })

    return render(request, 'checkout/booking_summary.html', {
        'quote': quote,
        'rfq': rfq,
        'currency_form': currency_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })


@login_required
def checkout(request, quote_pk):
    """
    Create a Stripe PaymentIntent and render the Stripe checkout form.
    Amount is converted to smallest currency unit (pence/cents) for Stripe.
    """
    quote = get_object_or_404(Quote, pk=quote_pk)
    rfq = quote.quote_request

    # Ensure only the RFQ owner can access this page
    if rfq.user != request.user:
        messages.error(request, 'You do not have permission to view this.')
        return redirect('quotes:rfq_list')

    if request.method == 'POST':
        currency = request.POST.get('currency', 'GBP')

        # Stripe requires amount in smallest currency unit (e.g. pence for GBP)
        amount_in_smallest_unit = int(quote.proposed_price * 100)

        # Create Stripe PaymentIntent with metadata for reference
        intent = stripe.PaymentIntent.create(
            amount=amount_in_smallest_unit,
            currency=currency.lower(),
            metadata={
                'quote_id': quote.id,
                'user_id': request.user.id,
            }
        )

        # Create an Order record with pending status
        order = Order.objects.create(
            user=request.user,
            quote=quote,
            amount_paid=quote.proposed_price,
            currency=currency,
            stripe_payment_intent_id=intent.id,
            status='pending',
        )

        return render(request, 'checkout/checkout.html', {
            'quote': quote,
            'order': order,
            'currency': currency,
            'client_secret': intent.client_secret,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        })

    return redirect('checkout:booking_summary', quote_pk=quote.pk)


@login_required
def checkout_success(request, order_number):
    """
    Handle successful payment — mark order as paid and show confirmation.
    """
    order = get_object_or_404(Order, order_number=order_number, user=request.user)

    # Update order status to paid
    order.status = 'paid'
    order.save()

    messages.success(request, f'Payment successful! Your order number is {order.order_number}.')
    return render(request, 'checkout/success.html', {'order': order})
