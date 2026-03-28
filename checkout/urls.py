from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('summary/<int:quote_pk>/', views.booking_summary, name='booking_summary'),
    path('pay/<int:quote_pk>/', views.checkout, name='checkout'),
    path('success/<str:order_number>/', views.checkout_success, name='checkout_success'),
]
