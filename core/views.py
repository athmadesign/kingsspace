from django.shortcuts import render
from services.models import ServiceCategory

# Create your views here.
def home(request):
    top_services = ServiceCategory.objects.all()[:3]
    context = {
        'top_services': top_services,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def projects(request):
    return render(request, 'core/projects.html')

def service_detail(request):
    return render(request, 'core/service_detail.html')