from django.urls import path
from . import views

app_name = 'negotiations'

urlpatterns = [
    path('<int:quote_pk>/', views.thread, name='thread'),
    path('<int:quote_pk>/accept/', views.accept_quote, name='accept_quote'),
]
