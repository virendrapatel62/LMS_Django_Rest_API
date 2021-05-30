import rest_framework
from rest_framework import serializers
from chapter.serializers import ChapterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from chapter.models import Chapter, chapter_choises, chapter_choises_description, video_plateform_choises
# Create your views here.
from rest_framework.permissions import IsAdminUser
from core.permissions import isAdminUserOrReadOnly


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


class ChapterListCreateView(ListCreateAPIView):
    permission_classes = [isAdminUserOrReadOnly]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            request = self.request
            print(request.data)
            serializer = self.serializer_class(
                data=request.data, context={"request":  request})
            serializer.is_valid()
            return serializer

        return self.serializer_class(self.queryset.all(), many=True)
