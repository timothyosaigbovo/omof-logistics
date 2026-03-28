from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from quotes.models import Quote
from .models import NegotiationMessage
from .forms import MessageForm


@login_required
def thread(request, quote_pk):
    quote = get_object_or_404(Quote, pk=quote_pk)

    if not request.user.is_staff and quote.quote_request.user != request.user:
        messages.error(request, 'You do not have permission to view this thread.')
        return redirect('quotes:rfq_list')

    thread_messages = quote.messages.all()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.quote = quote
            msg.sender = request.user
            msg.is_admin = request.user.is_staff
            msg.save()

            rfq = quote.quote_request
            if rfq.status == 'quoted':
                rfq.status = 'negotiating'
                rfq.save()

            return redirect('negotiations:thread', quote_pk=quote.pk)

    return render(request, 'negotiations/thread.html', {
        'quote': quote,
        'thread_messages': thread_messages,
        'form': form,
    })


@login_required
def accept_quote(request, quote_pk):
    quote = get_object_or_404(Quote, pk=quote_pk)
    rfq = quote.quote_request

    if rfq.user != request.user:
        messages.error(request, 'You do not have permission to accept this quote.')
        return redirect('quotes:rfq_list')

    if request.method == 'POST':
        rfq.status = 'accepted'
        rfq.save()
        messages.success(request, 'Quote accepted! Please proceed to payment.')
        return redirect('checkout:booking_summary', quote_pk=quote.pk)

    return redirect('negotiations:thread', quote_pk=quote.pk)
