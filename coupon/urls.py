from django.contrib import admin
from django.urls import path

from .views import test_view
# /api/courses
urlpatterns = [
    path('test/', test_view, name='test-api')
]
