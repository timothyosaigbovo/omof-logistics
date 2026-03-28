from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):

    CURRENCY_CHOICES = [
        ('GBP', 'British Pound'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('NGN', 'Nigerian Naira'),
        ('CAD', 'Canadian Dollar'),
        ('GHS', 'Ghanaian Cedi'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=254, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address_line1 = models.CharField(max_length=254, blank=True)
    address_line2 = models.CharField(max_length=254, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = CountryField(blank_label='Select Country', blank=True)
    preferred_currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, default='GBP'
    )

    def __str__(self):
        return self.user.username
