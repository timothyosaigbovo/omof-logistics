from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from services.models import ServiceCategory, Service
from blog.models import BlogPost
from reviews.models import Testimonial


class Command(BaseCommand):
    help = 'Create superuser and sample data for production'

    def handle(self, *args, **kwargs):

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@omoflogistics.com', 'Admin@2026!')
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        else:
            self.stdout.write('Superuser already exists')

        cat1, _ = ServiceCategory.objects.get_or_create(
            slug='freight',
            defaults={'name': 'Freight Services', 'description': 'Air, ocean and inland freight solutions'}
        )
        cat2, _ = ServiceCategory.objects.get_or_create(
            slug='customs',
            defaults={'name': 'Customs and Clearance', 'description': 'Expert customs clearance services'}
        )

        services = [
            {'slug': 'air-freight', 'name': 'Air Freight', 'category': cat1,
             'description': 'Fast and reliable air freight services worldwide.'},
            {'slug': 'ocean-freight', 'name': 'Ocean Freight', 'category': cat1,
             'description': 'Cost-effective ocean freight for large shipments.'},
            {'slug': 'inland-transport', 'name': 'Inland Transport', 'category': cat1,
             'description': 'Reliable inland transport connecting ports to destinations.'},
            {'slug': 'customs-clearance', 'name': 'Customs Clearance', 'category': cat2,
             'description': 'Hassle-free customs clearance handled by our expert team.'},
            {'slug': 'goods-protection', 'name': 'Goods Protection', 'category': cat2,
             'description': 'Comprehensive cargo insurance for complete peace of mind.'},
        ]
        for s in services:
            Service.objects.get_or_create(slug=s['slug'], defaults={
                'name': s['name'], 'category': s['category'],
                'description': s['description'], 'is_active': True
            })

        admin_user = User.objects.get(username='admin')
        BlogPost.objects.get_or_create(slug='welcome-to-omofo-logistics', defaults={
            'title': 'Welcome to Omofo Logistics',
            'author': admin_user,
            'body': 'We are excited to launch our new platform. Omofo Logistics offers bespoke freight forwarding, customs clearance and shipping services across Africa and beyond.',
            'is_published': True
        })

        testimonials = [
            {'author_name': 'James Okafor', 'company': 'Lagos Imports Ltd',
             'body': 'Omofo Logistics handled our shipment from London to Lagos flawlessly.'},
            {'author_name': 'Sarah Mitchell', 'company': 'UK Export Co',
             'body': 'The customs clearance team are exceptional. Completely stress-free.'},
            {'author_name': 'Kwame Asante', 'company': 'Accra Trading',
             'body': 'We have used Omofo three times now. Always on time and communicative.'},
        ]
        for t in testimonials:
            Testimonial.objects.get_or_create(author_name=t['author_name'], defaults={
                'company': t['company'], 'body': t['body'], 'is_featured': True
            })

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
