from django.urls import path
from . import views

urlpatterns = [
    path('services', views.service, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('services/<slug:category_slug>/<slug:sub_slug>/', views.sub_service_detail, name='sub_service_detail'),
]
