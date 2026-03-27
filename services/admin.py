from django.contrib import admin
from .models import ServiceCategory, Service


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'base_price', 'estimated_days', 'is_active')
    list_filter = ('category', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
```

Save. Commit:
```
git add .; git commit -m "Register ServiceCategory and Service in admin with filters and slug auto-fill"; git push origin main
```

---

Now let's add the real Omof Logistics services. Start the server:
```
python manage.py runserver
```

Go to **http://127.0.0.1:8000/admin/** and log in. You'll see **Services** in the sidebar now. We need to add data:

**First, add 3 Service Categories** (click Service Categorys > Add):

| Name | Slug | Description |
|------|------|-------------|
| Transport | transport | Freight and shipping services across air, sea, and land |
| Clearing & Protection | clearing-protection | Customs clearance and cargo protection services |
| Logistics Management | logistics-management | End-to-end supply chain and logistics solutions |

**Then add 9 Services** (click Services > Add):

| Name | Category | Base Price | Est. Days |
|------|----------|-----------|-----------|
| Air Freight | Transport | 500.00 | 3 |
| Ocean Freight | Transport | 250.00 | 21 |
| Inland Transport | Transport | 150.00 | 5 |
| LCL Shipping | Transport | 200.00 | 28 |
| Custom Services | Clearing & Protection | 300.00 | 7 |
| Goods Protection | Clearing & Protection | 100.00 | 1 |
| Industrial Logistics | Logistics Management | 400.00 | 10 |
| Omof Ecommerce | Logistics Management | 350.00 | 7 |
| Supply Chain Logistics | Logistics Management | 450.00 | 14 |
