from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='service_category/thumbnails/', blank=True, null=True)
    image = models.ImageField(upload_to='service_category/', blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title