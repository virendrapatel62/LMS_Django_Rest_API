from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
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
    '''
    Returns the list of courses , ordering by all fiels, searching by title , description, tagline, slud
    Sample url : domain.com/api/?tag=javascript&category=04557884-debd-4734-b52b-d47c1278d315&ordering=-title
    '''
    permission_classes = [isAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    search_fields = ['title', 'description', 'tagline', 'slug']
    ordering_fields = '__all__'
    filterset_fields = ['category', 'slug',
                        'price', 'discount', 'duration', 'title']
    queryset = Course.objects.filter(active=True)

    def get_serializer_context(self):
        context = super().get_serializer_context()

        return context

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        if tag is not None:
            courses = Tag.objects.filter(tag=tag).values_list('course')
            return self.queryset.filter(pk__in=courses)
        return self.queryset

    def create(self, request, *args, **kwargs):
        course = request.data
        category_id = course.get('category_id')
        # course.pop('category_id')

        category = None
        if category_id is None:
            return Response({'category_id': ['category_id is required.']}, status=HTTP_400_BAD_REQUEST)

        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist or ValidationError:
            return Response({'category_id': ['category_id is not valid.']}, status=HTTP_400_BAD_REQUEST)

        serializer = CourseSerializer(data=course)
        if(serializer.is_valid()):
            courseInstance = Course(
                **serializer.validated_data, category=category)

            courseInstance.save()
            return Response(CourseSerializer(courseInstance).data)

        return Response(serializer.errors,  status=HTTP_400_BAD_REQUEST)


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminUserOrReadOnly]
    lookup_field = 'slug'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    permission_classes = [isAdminUserOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def create(self, request, *args, **kwargs):
        tag = request.data
        course_id = tag.get('course')
        course = None
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist or ValidationError:
            return Response({'course': ["course id is invalid"]})

        serializer = TagSerializer(data=tag)
        if serializer.is_valid():
            tag = Tag(**serializer.validated_data, course=course)
            tag.save()
            return Response(TagSerializer(tag).data)
        else:
            return Response(serializer.errors)


class CourseByCategoryView(APIView):
    def get(self, request, category_id):
        try:
            courses = Course.objects.filter(category=Category(pk=category_id))
        except ValidationError:
            return Response({"course_id": ["Course Id is Not Valid"]}, status=HTTP_400_BAD_REQUEST)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
