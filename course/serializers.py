
from django.db import models
from django.db.models import fields
from .models import Course, Category, Tag
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
