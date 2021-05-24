
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/courses', include('course.urls')),
    path('api/chapters', include('chapter.urls')),
    path('api/coupons', include('coupon.urls')),
    path('api/doubts', include('doubt.urls')),
    path('api/orders', include('order.urls')),
    path('api/review', include('review.urls')),
]
