from rest_framework import serializers
from course.models import Category, Course, Tag
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from course.serializers import CategorySerializer, CourseSerializer, TagSerializer
from rest_framework.parsers import JSONParser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategorySlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CourseViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
