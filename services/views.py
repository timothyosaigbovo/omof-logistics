from django.shortcuts import render, get_object_or_404
from .models import ServiceCategory, Service


def service_list(request):
    """Display all services, optionally filtered by category"""
    services = Service.objects.filter(is_active=True)
    categories = ServiceCategory.objects.all()
    selected_category = None

    category_slug = request.GET.get('category')
    if category_slug:
        selected_category = get_object_or_404(ServiceCategory, slug=category_slug)
        services = services.filter(category=selected_category)

    context = {
        'services': services,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'services/service_list.html', context)


def service_detail(request, slug):
    """Display a single service"""
    service = get_object_or_404(Service, slug=slug, is_active=True)

    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)