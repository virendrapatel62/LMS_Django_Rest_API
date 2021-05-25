from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def test_view(request):
    response = {
        'message': 'Api is working.',
        'url': request.get_full_path()
    }
    return Response(response)
