from django.db import models
from django.contrib.auth.models import User
from quotes.models import Quote


class NegotiationMessage(models.Model):
    quote = models.ForeignKey(
        Quote, on_delete=models.CASCADE, related_name='messages'
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='negotiation_messages'
    )
    message = models.TextField()
    is_admin = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sent_at']

    def __str__(self):
        role = 'Admin' if self.is_admin else 'Client'
        return f"{role} message on Quote #{self.quote.pk} at {self.sent_at:%d %b %Y %H:%M}"
