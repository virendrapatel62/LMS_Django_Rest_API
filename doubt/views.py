from doubt.serializers import DoubtSerializer
from doubt.models import Doubt
from django.db.models.base import Model
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class DoubtModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Doubt.objects.all()
    serializer_class = DoubtSerializer
