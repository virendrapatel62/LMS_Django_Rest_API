from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.serializers import UserSerializer
from coupon.serializers import CouponSerializer
from django.db.models.base import Model
from order import models
from course.models import Course
from coupon.models import Coupon
from rest_framework.serializers import ModelSerializer, CharField, UUIDField, Serializer


class OrderCreateSerializer(Serializer):
    courses = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), many=True, required=False)
    course = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), required=False)
    coupon = serializers.CharField(required=False)

    def validate(self, attrs):

        error = ValidationError(
            {
                "course": "course or courses any one is required at a time.",
                "courses": "course or courses any one is required at a time."
            }
        )
        data = dict(attrs)
        courses = data.get('courses')
        course = data.get('course')
        coupon_code = data.get('coupon')

        if (course and courses) or (not course and not courses):
            raise error

        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code)
            except Coupon.DoesNotExist:
                raise ValidationError({"coupon": "Coupon is not valid"})

        return super().validate(attrs)


class OrderSerializer(ModelSerializer):
    order_id = CharField(max_length=30, required=False)
    user = UserSerializer(read_only=True)
    coupon = CouponSerializer(read_only=True)

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
