from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """Stores extra information about each user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=254, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address_line1 = models.CharField(max_length=254, blank=True)
    address_line2 = models.CharField(max_length=254, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = CountryField(blank_label='Select Country', blank=True)

    def __str__(self):
        return self.user.username