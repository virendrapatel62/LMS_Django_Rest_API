from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chapter.models import chapter_choises, chapter_choises_description, video_plateform_choises
# Create your views here.


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
