
from course.models import Course
from rest_framework.exceptions import ValidationError
from review.serializer import ReviewSerializer
from rest_framework.utils import serializer_helpers
from review.models import Review
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAuthenticated


class CanAddOwnReview(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'POST':
            logged_in_user = str(request.user.pk)
            body_user = request.data.get('user')
            if logged_in_user != body_user:
                raise ValidationError({"user": "User is not valid"})
            return super().has_permission(request, view)

        return True


class CanAddOrUpdateReviewOnEnrolledCourseOnly(BasePermission):
    def has_permission(self, request, view):
        method = request.method
        if method in ['PUT', 'POST']:
            user = request.user
            course_pk = request.data.get('course')

            if method == 'POST':

                message = {
                    "course": "Cant add review in this course , you are not enrolled."}

            if method == 'PUT':
                message = {
                    "course": "Cant update review in this course , you are not enrolled."}

            if user.subscriptions.filter(course=Course(pk=course_pk)).count() == 0:
                raise ValidationError(
                    message
                )
        return True


class CanDeleteOwnReview(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            review_pk = view.kwargs.get('pk')
            if Review.objects.filter(pk=review_pk, user=request.user).count() == 0:
                raise ValidationError(
                    {'details': 'you are not authorized to delete tis review'})

        return True


class ReviewViewSet(ModelViewSet):

    permission_classes = [(IsAuthenticated & CanAddOwnReview),
                          (IsAuthenticated & CanAddOrUpdateReviewOnEnrolledCourseOnly),
                          (IsAuthenticated & CanDeleteOwnReview)]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# can delete review only owned by user
