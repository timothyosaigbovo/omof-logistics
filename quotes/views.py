from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import QuoteRequest
from .forms import QuoteRequestForm


@login_required
def rfq_create(request):
    # Handle RFQ form submission
    service_id = request.GET.get('service')
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST, service_id=service_id)
        if form.is_valid():
            rfq = form.save(commit=False)
            rfq.user = request.user
            rfq.save()
            messages.success(
                request,
                'Your quote request has been submitted. We will be in touch shortly.'
            )
            return redirect('quotes:rfq_detail', pk=rfq.pk)
    else:
        form = QuoteRequestForm(service_id=service_id)
    return render(request, 'quotes/rfq_form.html', {'form': form})


@login_required
def rfq_detail(request, pk):
    # Show a single RFQ — only accessible by the owner
    try:
        rfq = QuoteRequest.objects.get(pk=pk, user=request.user)
    except QuoteRequest.DoesNotExist:
        messages.error(request, 'Quote request not found or you do not have permission to view it.')
        return redirect('quotes:rfq_list')
    return render(request, 'quotes/rfq_detail.html', {'rfq': rfq})


@login_required
def rfq_list(request):
    # List all RFQs belonging to the logged-in user
    rfqs = QuoteRequest.objects.filter(user=request.user)
    return render(request, 'quotes/rfq_list.html', {'rfqs': rfqs})


@login_required
def rfq_delete(request, pk):
    # Allow user to delete a pending RFQ only
    try:
        rfq = QuoteRequest.objects.get(pk=pk, user=request.user)
    except QuoteRequest.DoesNotExist:
        messages.error(request, 'Quote request not found or you do not have permission to delete it.')
        return redirect('quotes:rfq_list')
    if rfq.status != 'pending':
        messages.error(request, 'Only pending quote requests can be deleted.')
        return redirect('quotes:rfq_detail', pk=rfq.pk)
    if request.method == 'POST':
        rfq.delete()
        messages.success(request, 'Quote request deleted successfully.')
        return redirect('quotes:rfq_list')
    return render(request, 'quotes/rfq_confirm_delete.html', {'rfq': rfq})
