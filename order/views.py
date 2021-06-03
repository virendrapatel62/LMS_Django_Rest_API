import razorpay
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
from shortuuid import ShortUUID
KEY = "rzp_test_pSBqMZhMIjiLvk"
SECRET = "LSv5qER66R1ZA1niFvkRWSHf"


class CreateOrderApiView(APIView):
    permission_classes = [IsAuthenticated]

    def createRazorPayOrder(self, user, amount):
        client = razorpay.Client(auth=(KEY, SECRET))
        data = {
            "amount": int(amount*100),
            "currency": "INR",
            "receipt": f'feelfreetocode-{ShortUUID().random(length=6).upper()}',
            "notes": {
                "id": user.id,
                "username": user.username,
            }
        }
        order = client.order.create(data=data)
        return order

    def post(self, request):
        print("------- Post Request --------")
        data = JSONParser().parse(request)
        serializer = OrderCreateSerializer(data=data)
        if serializer.is_valid():
            data = serializer.validated_data
            course = data.get('course')
            body_courses = data.get('courses')
            courses = []
            if course:
                courses = [course]

            if body_courses:
                courses = body_courses

            total_price = 0
            after_discount_total_price = 0
            for course in courses:
                total_price += course.price
                sell_price = course.price - (course.price *
                                             course.discount * 0.01)
                after_discount_total_price += sell_price

            print('TOTAL PRICE : ', total_price)
            print('TOTAL PRICE  After Discount: ', after_discount_total_price)

            rp_order = self.createRazorPayOrder(
                request.user, after_discount_total_price)

            return Response(rp_order)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
