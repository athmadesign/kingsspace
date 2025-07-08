from django.shortcuts import render
from . models import ServiceCategory
from django.shortcuts import render, get_object_or_404
# Create your views here.

def service(request):
    categories = ServiceCategory.objects.all()
    context = {'categories': categories}  
    return render(request, 'core/services.html', context)

def service_detail(request, pk):
    category = get_object_or_404(ServiceCategory, pk=pk)
    services = category.services.all()  # Uses the related_name in your model
    context = {
        'category': category,
        'services': services,
    }
    return render(request, 'core/service_detail.html', context)