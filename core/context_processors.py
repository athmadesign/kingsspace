from services.models import ServiceCategory

def footer_service_categories(request):
    categories = ServiceCategory.objects.all()
    return {'footer_service_categories': categories}
