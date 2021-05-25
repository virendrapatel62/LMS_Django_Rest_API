from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import test_view
from .views import CategoryViewSet, CourseViewSet, TagViewSet
from rest_framework.routers import DefaultRouter
# /api/

category_router = DefaultRouter()
category_router.register('', CategoryViewSet, basename='category')

course_router = DefaultRouter()
course_router.register('', CourseViewSet, basename='course')

tag_router = DefaultRouter()
tag_router.register('', TagViewSet, basename='tag')


urlpatterns = [
    path('test/', test_view, name='test-api'),

    path('categories/', include(category_router.urls)),
    path('courses/', include(course_router.urls)),
    path('tags/', include(tag_router.urls)),

    # path('categories/', CategoryListView.as_view(), name='category-listview'),
    # path('categories/<str:pk>', CategoryDetailView.as_view(),
    #      name='category-detailview'),
]
