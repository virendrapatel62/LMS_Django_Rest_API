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


@api_view(['GET'])
def test_view(request):
    response = {
        'message': 'Api is working.',
        'url': request.get_full_path()
    }
    return Response(response)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
