from django.test import TestCase, Client
from django.urls import reverse
from .models import ServiceCategory, Service


class ServiceModelTest(TestCase):

    def setUp(self):
        self.category = ServiceCategory.objects.create(
            name='Freight', slug='freight', description='Freight services'
        )
        self.service = Service.objects.create(
            category=self.category,
            name='Air Freight',
            slug='air-freight',
            description='Fast air freight service',
            is_active=True
        )

    def test_service_str(self):
        self.assertEqual(str(self.service), 'Air Freight')

    def test_service_category_str(self):
        self.assertEqual(str(self.category), 'Freight')

    def test_service_list_view(self):
        client = Client()
        response = client.get(reverse('services:service_list'))
        self.assertEqual(response.status_code, 200)

    def test_service_detail_view(self):
        client = Client()
        response = client.get(reverse('services:service_detail', args=['air-freight']))
        self.assertEqual(response.status_code, 200)
