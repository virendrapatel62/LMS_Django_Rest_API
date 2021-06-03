from order.views import CreateOrderApiView
from django.contrib import admin
from django.urls import path

# /api/orders
urlpatterns = [
    path('create/', CreateOrderApiView.as_view(), name='order-create')
]
