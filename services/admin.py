from django.contrib import admin
from .models import ServiceCategory, Service

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Service)
class  ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
