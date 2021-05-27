
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Course, Category, Tag
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class TagSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'
