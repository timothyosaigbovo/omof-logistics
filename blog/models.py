# blog/models.py
# BlogPost model for the Omofo Logistics news and insights section.
# Posts are managed via the Django admin panel by staff.

from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """
    Represents a published blog article.
    Only posts with is_published=True are shown on the public blog page.
    Slug is used for SEO-friendly URLs.
    """

    title = models.CharField(max_length=200)
    # URL-friendly version of the title — must be unique
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    # Optional featured image stored in AWS S3 in production
    image = models.ImageField(upload_to='blog/', blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return the canonical URL for this blog post."""
        from django.urls import reverse
        return reverse('blog:post_detail', args=[self.slug])
