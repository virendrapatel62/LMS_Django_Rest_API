from course.models import Category, Course, Tag
from rest_framework.status import HTTP_400_BAD_REQUEST
from course.serializers import CategorySerializer, CourseSerializer, TagSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from core.permissions import isAdminUserOrReadOnly


class CategoryViewSet(ModelViewSet):
    permission_classes = [isAdminUserOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategorySlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminUserOrReadOnly]
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CourseViewSet(ModelViewSet):
    permission_classes = [isAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminUserOrReadOnly]
    lookup_field = 'slug'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    permission_classes = [isAdminUserOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
