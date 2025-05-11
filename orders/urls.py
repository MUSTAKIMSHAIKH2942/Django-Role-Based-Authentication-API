# orders/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('list/', views.order_list, name='order_list'),
]
