from django.db.models.base import Model
from order import models
from rest_framework.serializers import ModelSerializer, CharField, UUIDField


class OrderSerializer(ModelSerializer):
    order_id = CharField(max_length=30, required=False)
    user = UUIDField(required=False)

    class Meta:
        model = models.Order
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = '__all__'
