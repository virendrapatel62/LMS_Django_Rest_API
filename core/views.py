from order.models import Subscription
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.reverse import reverse
from review.models import Review
from rest_framework_simplejwt.views import TokenObtainPairView
from core.serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def api_root(request):
    response = {
        "API Root": reverse('api_root', request=request),
        "Auth Tokne": {
            "Access Token": reverse('token_obtain_pair', request=request),
            "Token Refresh": reverse('token_refresh', request=request),
            "Token Verify": reverse('token_verify', request=request),
        },
        "Course": {
            "Course List": reverse('course:course-list', request=request),
            "Course Detail": reverse('course:course-detail', args=[1], request=request),
            "Course Detail By Slug": reverse('course:course-detail-by-slug', args=['course-slug'], request=request),
            "Courses By Category Id": reverse('course:courses-by-category', args=['category-id'], request=request),
        },

        "Tags": {
            "Tag List": reverse('course:tag-list', request=request),
            "Tag Detail": reverse('course:tag-detail', args=[2], request=request),

        },

        "Category": {
            "Category List": reverse('course:category-list', request=request),
            "Category Detail": reverse('course:category-detail', args=[4], request=request),
            "Category Detail By Slug": reverse('course:category-detail-by-slug', args=['category-slug'], request=request),
        },
        "Chapter": {
            "Chapter Types": reverse('chapter:chapter-type-view', request=request),
            "Video Plateform List": reverse('chapter:video-plateform-listview', request=request),
            "Chapter Create": reverse('chapter:chapter-createview', request=request),
            "Chapter Detail": reverse('chapter:chapter-detailview', args=['chapter_id'],  request=request),
            "Chapter By Course": reverse('chapter:chapter-listview', args=['course-id'],  request=request),
        },
        "Coupon": {
            "Coupon List": reverse('coupon:coupon-list', request=request),
            "Coupon Detail": reverse('coupon:coupon-detail', args=['pk'],  request=request),
            "Coupon By Code": reverse('coupon:coupon-by-code', args=['course_id', 'code'],  request=request),
        },
        "Orders": {
            "CReate Order": reverse("order:order-create", request=request),
            "Verify Order": reverse("order:order-verify", request=request),
        },
        "Subscriptions": {
            "List": reverse("subscription:subscription-list", request=request),
            "SUbscribed Courses Of Users": reverse("subscription:subscription-list-of-user", args=['1'],  request=request),
        },
        "Review": {
            "List": reverse("review:review-list", request=request),
            "Detail": reverse("review:review-detail", args=["PK"], request=request),
        },
        "Doubt": {
            "List": reverse("doubt:doubt-list", request=request),
            "Detail": reverse("doubt:doubt-detail", args=["PK"], request=request),
        }


    }
    return Response(response)


