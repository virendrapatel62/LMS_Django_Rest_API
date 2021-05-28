from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chapter.models import chapter_choises, chapter_choises_description
# Create your views here.


@api_view(['GET'])
def chapter_types_view(request):

    def searchDescription(id):
        for _id, description in chapter_choises_description:
            if id == _id:
                return description

    def changeToDict(chapter_type):
        id, type = chapter_type
        return {
            "id": id,
            "type": type,
            'description': searchDescription(id)
        }
    types = map(changeToDict, chapter_choises)
    return Response(types)
