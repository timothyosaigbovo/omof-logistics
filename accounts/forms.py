from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """Form for users to edit their profile"""
    class Meta:
        model = UserProfile
        fields = ['company_name', 'phone', 'address_line1',
                  'address_line2', 'city', 'country']