from django.urls import path
from . import views

urlpatterns = [
    path('services', views.service, name='services'),
    path('services/<int:pk>/', views.service_detail, name='service_detail')
]
