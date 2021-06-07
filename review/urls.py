from django.contrib import admin
from django.db.models import base
from django.urls import path
from review.views import ReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ReviewViewSet, basename='review')

urlpatterns = router.urls
