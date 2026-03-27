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
    """Individual services like Air Freight, Ocean Freight, etc."""
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name='services'
    )
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_days = models.IntegerField(
        help_text='Estimated delivery time in days'
    )
    image = models.ImageField(upload_to='services/', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name