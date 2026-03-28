from django.contrib import admin
from .models import QuoteRequest, Quote


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'origin', 'destination', 'urgency', 'status', 'submitted_at')
    list_filter = ('status', 'urgency')
    search_fields = ('user__username', 'origin', 'destination')
    readonly_fields = ('submitted_at',)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'quote_request', 'proposed_price', 'currency', 'valid_until', 'issued_at')
    readonly_fields = ('issued_at',)
