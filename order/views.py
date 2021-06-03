from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status
from order.serializers import OrderCreateSerializer, OrderItemSerializer, OrderSerializer, SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated
from coupon.models import Coupon


class CreateOrderApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = JSONParser().parse(request)
        print(data, data)
        serializer = OrderCreateSerializer(data=data)
        if serializer.is_valid():
            print("Validated Data", serializer.validated_data)
            return Response('ok')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
