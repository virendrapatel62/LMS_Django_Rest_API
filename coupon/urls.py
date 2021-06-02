from django.contrib import admin
from django.db.models import base
from django.urls import path
from django.urls.conf import include
from coupon.views import CouponRetrieveViewByCode
from coupon.views import CouponModelViewSet
from rest_framework.routers import DefaultRouter
# /api/coupons

coupon_router = DefaultRouter()
coupon_router.register("", CouponModelViewSet, basename='coupon')

urlpatterns = [
    path('course/<str:course_id>/code/<str:code>/',
         CouponRetrieveViewByCode.as_view(), name='coupon-by-code'),

    path('', include(coupon_router.urls))
]
