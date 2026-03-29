# services/models.py
# Models for the services catalogue.
# Services are grouped into categories and displayed without prices.
# All pricing is handled via the Request for Quote (RFQ) flow.

from django.db import models


class ServiceCategory(models.Model):
    """
    Groups related services together e.g. Air Freight, Ocean Freight.
    Used to organise the services listing page by category.
    """

    name = models.CharField(max_length=254)
    # URL-friendly identifier for the category
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField()
    # Optional category image stored in AWS S3 in production
    image = models.ImageField(upload_to='categories/', blank=True)

    class Meta:
        verbose_name_plural = 'Service Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    """
    Represents an individual logistics service offered by Omofo Logistics.
    Examples: Air Freight, Ocean Freight, Customs Clearance.
    No price fields — all pricing is handled via the Request for Quote flow.
    Only active services are shown on the public services page.
    """

    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name='services'
    )
    name = models.CharField(max_length=254)
    # URL-friendly identifier used in service detail URLs
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField()
    # Optional service image stored in AWS S3 in production
    image = models.ImageField(upload_to='services/', blank=True)
    # Inactive services are hidden from the public listing
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return the canonical URL for this service detail page."""
        from django.urls import reverse
        return reverse('services:service_detail', args=[self.slug])
