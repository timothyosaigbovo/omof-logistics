from django.shortcuts import render, get_object_or_404
from .models import ServiceCategory, Service


def service_list(request):
    categories = ServiceCategory.objects.prefetch_related('services').filter(
        services__is_active=True
    ).distinct()
    return render(request, 'services/service_list.html', {
        'categories': categories
    })


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    return render(request, 'services/service_detail.html', {
        'service': service
    })