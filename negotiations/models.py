# negotiations/models.py
# Stores messages exchanged between client and admin during quote negotiation.

from django.db import models
from django.contrib.auth.models import User
from quotes.models import Quote


class NegotiationMessage(models.Model):
    """
    Represents a single message in a negotiation thread linked to a Quote.
    The is_admin flag distinguishes between client and admin messages
    so the thread can display them differently in the UI.
    Messages are ordered chronologically by sent_at.
    """

    quote = models.ForeignKey(
        Quote, on_delete=models.CASCADE, related_name='messages'
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='negotiation_messages'
    )
    message = models.TextField()
    # True if the sender is an admin/staff member
    is_admin = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sent_at']

    def __str__(self):
        role = 'Admin' if self.is_admin else 'Client'
        return f"{role} message on Quote #{self.quote.pk} at {self.sent_at:%d %b %Y %H:%M}"
