from doubt.serializers import DoubtSerializer
from doubt.models import Doubt
from django.db.models.base import Model
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
# Create your views here.


class CanDeleteAndUpdateOnlyOwnDoubt(BasePermission):
    def has_permission(self, request, view):
        method = request.method
        if method in ['PUT', "DELETE", "PATCH"]:
            user = request.user
            if user.is_superuser:
                return True

            doubt_id = view.kwargs.get('pk')
            try:
                doubt = Doubt.objects.get(pk=doubt_id)
            except Doubt.DoesNotExist:
                return Response({"details": "doubt not found"}, status=400)
            return doubt.user == user

        return True


class DoubtModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,
                          CanDeleteAndUpdateOnlyOwnDoubt]
    queryset = Doubt.objects.all()
    serializer_class = DoubtSerializer
