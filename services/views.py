from django.shortcuts import render
from . models import ServiceCategory, Service
from django.shortcuts import render, get_object_or_404
# Create your views here.

def service(request):
    categories = ServiceCategory.objects.all()
    context = {'categories': categories}  
    return render(request, 'core/services.html', context)

def service_detail(request, slug):
    category = get_object_or_404(ServiceCategory, slug=slug)
    services = category.services.all()  # Uses the related_name in your model
    context = {
        'category': category,
        'services': services,
    }
    return render(request, 'core/service_detail.html', context)

def sub_service_detail(request, category_slug, sub_slug):
    category = get_object_or_404(ServiceCategory, slug=category_slug)
    sub_service = get_object_or_404(Service, slug=sub_slug, category=category)
    
    context = {
        'category': category,
        'service': sub_service,
    }
    return render(request, 'core/sub_services.html', context)