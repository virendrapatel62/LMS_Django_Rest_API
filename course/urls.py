from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import CategorySlugDetailView, CategoryViewSet,  CourseByCategoryView, CourseSlugDetailView, CourseViewSet, TagViewSet
from rest_framework.routers import DefaultRouter
# /api/

category_router = DefaultRouter()
category_router.register('', CategoryViewSet, basename='category')

course_router = DefaultRouter()
course_router.register('', CourseViewSet, basename='course')

tag_router = DefaultRouter()
tag_router.register('', TagViewSet, basename='tag')
# tag-list
# tag-detail

# /api/course

urlpatterns = [


    path('categories/slug/<str:slug>/', CategorySlugDetailView.as_view(),
         name='category-detail-by-slug'),

    path('categories/', include(category_router.urls)),
    path('categories/<str:category_id>/courses/',
         CourseByCategoryView.as_view(), name='courses-by-category'),

    path('tags/', include(tag_router.urls)),


    path('courses/', include(course_router.urls)),
    path('slug/<str:slug>/', CourseSlugDetailView.as_view(),
         name='course-detail-by-slug'),


    # path('categories/', CategoryListView.as_view(), name='category-listview'),
    # path('categories/<str:pk>', CategoryDetailView.as_view(),
    #      name='category-detailview'),
]
