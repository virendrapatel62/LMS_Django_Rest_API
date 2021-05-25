
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('course.urls')),
    path('api/chapters/', include('chapter.urls')),
    path('api/coupons/', include('coupon.urls')),
    path('api/doubts/', include('doubt.urls')),
    path('api/orders/', include('order.urls')),
    path('api/reviews/', include('review.urls')),
]
