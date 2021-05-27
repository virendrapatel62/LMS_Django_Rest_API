from django.core.exceptions import ValidationError
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        course = request.data
        category_id = course.get('category_id')
        # course.pop('category_id')

        category = None
        if category_id is None:
            return Response({'category_id': ['category_id is required.']})

        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist or ValidationError:
            return Response({'category_id': ['category_id is not valid.']})

        serializer = CourseSerializer(data=course)
        if(serializer.is_valid()):
            courseInstance = Course(
                **serializer.validated_data, category=category)

            courseInstance.save()
            return Response(CourseSerializer(courseInstance).data)

        return Response(serializer.errors)


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminUserOrReadOnly]
    lookup_field = 'slug'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    permission_classes = [isAdminUserOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
