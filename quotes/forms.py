from django import forms
from .models import QuoteRequest


class QuoteRequestForm(forms.ModelForm):

    class Meta:
        model = QuoteRequest
        fields = [
            'service', 'origin', 'destination', 'cargo_description',
            'estimated_weight_kg', 'urgency', 'special_requirements'
        ]
        widgets = {
            'cargo_description': forms.Textarea(attrs={'rows': 4}),
            'special_requirements': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'estimated_weight_kg': 'Estimated weight (kg)',
            'special_requirements': 'Special requirements (optional)',
        }

    def __init__(self, *args, **kwargs):
        service_id = kwargs.pop('service_id', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['urgency'].widget.attrs['class'] = 'form-select'
        self.fields['service'].widget.attrs['class'] = 'form-select'
        if service_id:
            self.fields['service'].initial = service_id