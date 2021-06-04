from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from course.models import Course
from chapter.serializers import ChapterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from chapter.models import Chapter, chapter_choises, chapter_choises_description, video_plateform_choises
# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from core.permissions import isAdminUserOrReadOnly
import uuid


@api_view(['GET'])
def chapter_types_view(request):

    def searchDescription(id):
        for _id, description in chapter_choises_description:
            if id == _id:
                return description

    types = map(lambda e: dict(
        id=e[0], type=e[1], description=searchDescription(e[0])), chapter_choises)
    return Response(types)


@api_view(['GET'])
def video_plateform_view(request):

    plateforms = map(lambda e: dict(
        id=e[0], plateform=e[1]), video_plateform_choises)
    return Response(plateforms)


class ChapterListView(ListAPIView):
    # we wiil add persmission only user who purched this course
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    ordering = ['index']

    def get(self, request, *args, **kwargs):
        try:
            course = self.kwargs.get('course')
            uuid.UUID(course)
        except:
            return Response({"course": ["Course id is not valid"]}, status=status.HTTP_400_BAD_REQUEST)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        course = self.kwargs.get('course')
        return Chapter.objects.filter(parent_chapter=None, course=Course(pk=course))


class ChapterCreateView(CreateAPIView):

    permission_classes = [IsAdminUser]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    # def get_queryset(self):
    #     return Chapter.objects.filter(parent_chapter=None)

    def get_serializer(self, *args, **kwargs):

        request = self.request
        print(request.data)
        serializer = self.serializer_class(
            data=request.data, context={"request":  request})
        serializer.is_valid()
        return serializer


class ChapterDetailView(APIView):
    def get(self, request, **kargs):
        chapter_id = kargs.get('pk')
        try:
            chapter = Chapter.objects.get(pk=chapter_id)
        except Chapter.DoesNotExist or ValidationError:
            return Response(status=404)
        #  user subscribed this course
        # then alwaays return full ojject data
        context = {
            "full": chapter.is_preview
        }
        serailizer = ChapterSerializer(chapter, context=context)
        return Response(serailizer.data)
