from course.models import Course
from rest_framework.exceptions import ValidationError
from review.serializer import ReviewSerializer
from rest_framework.utils import serializer_helpers
from review.models import Review
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
# Create your views here.


class CanAddOwnReview(BasePermission):
    def has_permission(self, request, view):

        if request.method == "GET":
            return True

        logged_in_user = str(request.user.pk)
        body_user = request.data.get('user')
        if logged_in_user != body_user:
            raise ValidationError({"user": "User is not valid"})
        return super().has_permission(request, view)


class CanAddReviewOnEnrolledCourseOnly(BasePermission):
    def has_permission(self, request, view):

        if request.method == "GET":
            return True

        user = request.user
        course_pk = request.data.get('course')

        if request.method == 'POST':
            message = {
                "course": "Cant add review in this course , you are not enrolled."}

        if request.method == 'PUT':
            message = {
                "course": "Cant update review in this course , you are not enrolled."}

        if user.subscriptions.filter(course=Course(pk=course_pk)).count() == 0:
            raise ValidationError(
                message
            )
        return super().has_permission(request, view)


class ReviewViewSet(ModelViewSet):
    permission_classes = [CanAddOwnReview, CanAddReviewOnEnrolledCourseOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# can delete review only owned by user
