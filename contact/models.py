# contact/models.py
# Stores contact form submissions from site visitors.
# Messages are visible in the Django admin panel for the team to action.

from django.db import models


class ContactMessage(models.Model):
    """
    Represents a message submitted via the contact form.
    is_read flag allows admin to track which messages have been actioned.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    # Allows admin to mark messages as read in the admin panel
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"{self.name} — {self.subject}"
