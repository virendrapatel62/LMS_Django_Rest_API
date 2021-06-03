from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status
from order.serializers import OrderItemSerializer, OrderSerializer, SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated


class CreateOrderApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.user)
        data = JSONParser().parse(request)
        orderSerializer = OrderSerializer(data=data)
        if orderSerializer.is_valid():
            return Response("Ok")
        else:
            return Response(orderSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
