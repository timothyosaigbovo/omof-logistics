# services/views.py
# Displays the services catalogue to site visitors.
# No prices are shown — visitors are directed to request a quote.

from django.shortcuts import render, get_object_or_404
from .models import ServiceCategory, Service


def service_list(request):
    """
    Display all active services grouped by category.
    Uses prefetch_related for efficient database querying.
    Only categories that have at least one active service are shown.
    """
    categories = ServiceCategory.objects.prefetch_related('services').filter(
        services__is_active=True
    ).distinct()

    return render(request, 'services/service_list.html', {
        'categories': categories
    })


def service_detail(request, slug):
    """
    Display the detail page for a single active service.
    Returns 404 if the service does not exist or is inactive.
    """
    service = get_object_or_404(Service, slug=slug, is_active=True)

    return render(request, 'services/service_detail.html', {
        'service': service
    })
