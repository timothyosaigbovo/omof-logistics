from django.db import models
from django.contrib.auth.models import User
from services.models import Service


class Testimonial(models.Model):
    author_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author_name} — {self.company}"
