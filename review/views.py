from review.serializer import ReviewSerializer
from rest_framework.utils import serializer_helpers
from review.models import Review
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
