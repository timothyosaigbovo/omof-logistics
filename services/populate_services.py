"""
Run this script with: python manage.py shell < services/populate_services.py
"""
from services.models import ServiceCategory, Service

# Clear existing data
Service.objects.all().delete()
ServiceCategory.objects.all().delete()

# === CREATE CATEGORIES ===
transport = ServiceCategory.objects.create(
    name='Transport',
    slug='transport',
    description='Freight and shipping services across air, sea, and land routes worldwide.'
)

clearing = ServiceCategory.objects.create(
    name='Clearing & Protection',
    slug='clearing-protection',
    description='Customs clearance, brokerage, and cargo protection services to keep your goods safe and compliant.'
)

logistics = ServiceCategory.objects.create(
    name='Logistics Management',
    slug='logistics-management',
    description='End-to-end supply chain, industrial logistics, and e-commerce fulfilment solutions.'
)

# === CREATE SERVICES ===

# Transport Services
Service.objects.create(
    category=transport,
    name='Air Freight',
    slug='air-freight',
    description='When speed is your top priority, Omof Logistics Air Freight offers the fastest and most secure solution for your cargo. We provide reliable air cargo services for time-sensitive shipments, connecting businesses to destinations worldwide with scheduled and charter flight options. Our air freight solutions include door-to-door delivery, airport-to-airport transfers, express and consolidated shipments, and dangerous goods handling.',
    base_price=500.00,
    estimated_days=3,
)

Service.objects.create(
    category=transport,
    name='Ocean Freight',
    slug='ocean-freight',
    description='Omof Logistics provides comprehensive ocean freight services connecting global trade routes with unmatched reliability and competitive pricing. Whether you are shipping full container loads or less-than-container loads, we offer flexible sea freight solutions tailored to your cargo needs. Our ocean freight services cover FCL and LCL shipments, port-to-port and door-to-door delivery, reefer container services for temperature-sensitive goods, and real-time cargo tracking.',
    base_price=250.00,
    estimated_days=21,
)

Service.objects.create(
    category=transport,
    name='Inland Transport',
    slug='inland-transport',
    description='We provide point-to-point delivery, cross-docking, intercity distribution, bulk transport, and scheduled route services across Nigeria and West Africa. Our inland transport fleet is equipped to handle goods of all sizes, from small parcels to heavy industrial equipment. We ensure timely and safe delivery with GPS-tracked vehicles and experienced logistics coordinators.',
    base_price=150.00,
    estimated_days=5,
)

Service.objects.create(
    category=transport,
    name='LCL Shipping',
    slug='lcl-shipping',
    description='Our Less-than-Container Load shipping service is designed for businesses that need to move smaller volumes of cargo without the cost of booking a full container. We consolidate your shipment with other cargo heading to the same destination, giving you access to global shipping routes at a fraction of the cost. LCL shipping is ideal for small and medium businesses, startups, and e-commerce sellers.',
    base_price=200.00,
    estimated_days=28,
)

# Clearing & Protection Services
Service.objects.create(
    category=clearing,
    name='Custom Services',
    slug='custom-services',
    description='Our Custom Services division is dedicated to helping clients navigate the complexities of international trade regulations and customs procedures. We handle all documentation, tariff classifications, duty calculations, and regulatory compliance to ensure your goods clear customs smoothly and efficiently. Our experienced customs brokers work directly with port authorities to minimise delays and avoid penalties.',
    base_price=300.00,
    estimated_days=7,
)

Service.objects.create(
    category=clearing,
    name='Goods Protection',
    slug='goods-protection',
    description='Our Goods Protection service ensures that all goods entrusted to us are handled with maximum care, security, and proper insurance coverage. From specialised packaging and crating to climate-controlled storage and secure transit, we take every precaution to protect your cargo throughout the supply chain. We offer comprehensive cargo insurance, tamper-proof sealing, real-time monitoring, and damage-free delivery guarantees.',
    base_price=100.00,
    estimated_days=1,
)

# Logistics Management Services
Service.objects.create(
    category=logistics,
    name='Industrial Logistics',
    slug='industrial-logistics',
    description='Omof Logistics Industrial Logistics solutions are built to support the complex operational needs of manufacturers, construction firms, and heavy industry. We manage the movement of raw materials, machinery, equipment, and finished products with precision and reliability. Our industrial logistics services include project cargo management, heavy lift and oversized transport, warehouse management, and just-in-time delivery.',
    base_price=400.00,
    estimated_days=10,
)

Service.objects.create(
    category=logistics,
    name='Omof Ecommerce',
    slug='omof-ecommerce',
    description='Omof Ecommerce Solution is a complete logistics ecosystem built to empower online retailers, marketplace sellers, and direct-to-consumer brands. We handle everything from warehousing and inventory management to order fulfilment, packaging, and last-mile delivery. Our e-commerce logistics platform integrates with major online marketplaces and provides real-time order tracking for your customers.',
    base_price=350.00,
    estimated_days=7,
)

Service.objects.create(
    category=logistics,
    name='Supply Chain Logistics',
    slug='supply-chain-logistics',
    description='Omof Logistics delivers comprehensive supply chain solutions designed to enhance efficiency, visibility, and control across your entire operation. From procurement and vendor management to distribution and reverse logistics, we optimise every link in your supply chain. Our solutions include demand forecasting, inventory optimisation, distribution network design, and end-to-end supply chain consulting.',
    base_price=450.00,
    estimated_days=14,
)

print('Successfully added 3 categories and 9 services!')