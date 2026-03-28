from django.contrib import admin
from .models import Shipment, ShipmentUpdate


class ShipmentUpdateInline(admin.TabularInline):
    model = ShipmentUpdate
    extra = 1
    readonly_fields = ('timestamp',)


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_reference', 'order', 'current_status', 'estimated_delivery', 'created_at')
    list_filter = ('current_status',)
    search_fields = ('tracking_reference', 'order__order_number')
    readonly_fields = ('created_at',)
    inlines = [ShipmentUpdateInline]
