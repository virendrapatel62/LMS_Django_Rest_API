from django.db.models import fields
from django.db.models.base import Model
from coupon.models import Coupon
from rest_framework.serializers import ModelSerializer


class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
