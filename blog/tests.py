from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BlogPost


class BlogTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.post = BlogPost.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            body='This is a test blog post.',
            is_published=True
        )

    def test_blog_list_view(self):
        client = Client()
        response = client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_view(self):
        client = Client()
        response = client.get(reverse('blog:post_detail', args=['test-post']))
        self.assertEqual(response.status_code, 200)

    def test_unpublished_post_not_visible(self):
        self.post.is_published = False
        self.post.save()
        client = Client()
        response = client.get(reverse('blog:post_detail', args=['test-post']))
        self.assertEqual(response.status_code, 404)
