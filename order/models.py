from django.db import models
from django.contrib.auth.models import User
from coupon.models import Coupon
from course.models import Course
import uuid
# Create your models here.

ORDER_STATUS_CHOICES = (
    ("S", "SUCCESS"),
    ("F", "FAIL"),
    ("I", "INITIATED")
)


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    order_id = models.CharField(max_length=100, null=False)
    payment_id = models.CharField(max_length=100, null=True)
    order_status = models.CharField(
        max_length=2, default="I", choices=ORDER_STATUS_CHOICES)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    time = models.DateTimeField(auto_now_add=True)
    coupon = models.ForeignKey(
        Coupon, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)


class OrderItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='order_items')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    coupon = models.ForeignKey(
        Coupon, on_delete=models.CASCADE, related_name="order_items", blank=True,  null=True)


class Subscription(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='subscriptions')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='subscriptions')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subscriptions')
    time = models.DateTimeField(auto_now_add=True)
