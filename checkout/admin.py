from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'amount_paid', 'currency', 'status', 'created_at')
    list_filter = ('status', 'currency')
    search_fields = ('order_number', 'user__email', 'stripe_payment_intent_id')
    readonly_fields = ('order_number', 'created_at')
