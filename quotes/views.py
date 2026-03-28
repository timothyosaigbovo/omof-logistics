from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import QuoteRequest
from .forms import QuoteRequestForm


@login_required
def rfq_create(request):
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
    rfq = get_object_or_404(QuoteRequest, pk=pk, user=request.user)
    return render(request, 'quotes/rfq_detail.html', {'rfq': rfq})


@login_required
def rfq_list(request):
    rfqs = QuoteRequest.objects.filter(user=request.user)
    return render(request, 'quotes/rfq_list.html', {'rfqs': rfqs})
