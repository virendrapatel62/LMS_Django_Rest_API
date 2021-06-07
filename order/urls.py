from order.views import CreateOrderApiView, SubscriptionListView, VerifyOrderApiView
from django.contrib import admin
from django.urls import path

# /api/orders
Orderurls = [
    path('create/', CreateOrderApiView.as_view(), name='order-create'),
    path('verify/', VerifyOrderApiView.as_view(), name='order-verify')
]

# /api/subscriptions/
subscriptionUrls = [
    path('', SubscriptionListView.as_view(), name='subscription-list')
]
