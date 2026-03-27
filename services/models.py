from django.db import models


class ServiceCategory(models.Model):
    """Categories like Transport, Clearing, Logistics Management"""
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/', blank=True)

    class Meta:
        verbose_name_plural = 'Service Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    """Individual services like Air Freight, Ocean Freight, etc.
    No price fields — all pricing is handled via Request for Quote."""
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name='services'
    )
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('services:service_detail', args=[self.slug])