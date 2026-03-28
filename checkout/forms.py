from django import forms


CURRENCY_CHOICES = [
    ('GBP', '£  GBP — British Pound'),
    ('USD', '$  USD — US Dollar'),
    ('EUR', '€  EUR — Euro'),
    ('NGN', '₦  NGN — Nigerian Naira'),
    ('CAD', 'CA$  CAD — Canadian Dollar'),
    ('GHS', 'GH₵  GHS — Ghanaian Cedi'),
]


class CurrencyForm(forms.Form):
    currency = forms.ChoiceField(
        choices=CURRENCY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'currency-select'})
    )
