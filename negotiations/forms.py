from django import forms
from .models import NegotiationMessage


class MessageForm(forms.ModelForm):

    class Meta:
        model = NegotiationMessage
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Type your message here...'
            })
        }
        labels = {
            'message': ''
        }
