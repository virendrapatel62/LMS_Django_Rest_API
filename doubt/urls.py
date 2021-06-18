from django.contrib import admin
from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns
from doubt.views import DoubtModelViewSet, DoubtAnswerModelViewSet
from rest_framework.routers import DefaultRouter
# root url : /api/doubts

doubtRouter = DefaultRouter()

doubtRouter.register(
    "answers", DoubtAnswerModelViewSet, basename='doubt-answer')
    
doubtRouter.register("", DoubtModelViewSet, basename='doubt')


urlpatterns = []

urlpatterns += doubtRouter.urls
