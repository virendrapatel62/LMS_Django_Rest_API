import rest_framework
from coupon.serializers import CouponSerializer
from coupon.models import Coupon
from course.models import Course
from typing import List
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from uuid import UUID
# /api/coupons

# /api/coupons/code/<code>


class CouponRetrieveViewByCode(ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def get(self, request, *args, **kwargs):
        code = self.kwargs.get('code')
        course_id = self.kwargs.get('course_id')
        try:
            UUID(course_id)
        except:
            return Response({"course": ["course id is not valid id"]}, status=status.HTTP_400_BAD_REQUEST)
        self.queryset = self.queryset.filter(course=Course(
            pk=course_id), code=code, active=True)
        if len(self.queryset) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return super().get(request, *args, **kwargs)


class CouponModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
