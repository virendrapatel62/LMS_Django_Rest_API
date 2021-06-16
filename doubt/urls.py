from django.contrib import admin
from django.db import router
from django.urls import path
from rest_framework import urlpatterns
from doubt.views import DoubtModelViewSet
from rest_framework.routers import DefaultRouter
# root url : /api/doubts

doubtRouter = DefaultRouter()
doubtRouter.register("", DoubtModelViewSet, basename='doubt')

urlpatterns = []
urlpatterns += doubtRouter.urls
