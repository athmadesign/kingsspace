
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    # path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
    path('service_detail', views.service_detail, name='service_detail')
]
