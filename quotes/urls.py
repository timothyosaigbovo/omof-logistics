from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.rfq_list, name='rfq_list'),
    path('request/', views.rfq_create, name='rfq_create'),
    path('<int:pk>/', views.rfq_detail, name='rfq_detail'),
]