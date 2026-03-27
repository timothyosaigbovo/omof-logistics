from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'phone', 'city', 'country')
    search_fields = ('user__username', 'company_name', 'phone')
    list_filter = ('country',)