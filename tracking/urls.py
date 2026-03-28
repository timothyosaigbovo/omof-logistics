from django.urls import path
from . import views

app_name = 'tracking'

urlpatterns = [
    path('<str:tracking_reference>/', views.tracking_detail, name='tracking_detail'),
]
