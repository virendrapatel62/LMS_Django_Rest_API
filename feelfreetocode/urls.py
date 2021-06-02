
from django.contrib import admin
from django.urls import path, include
from core.views import api_root

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/', api_root, name='api_root'),

    path('api/', include(('course.urls', 'course'), namespace='course')),

    path('api/chapters/', include(('chapter.urls', 'chapter'), namespace='chapter')),
    path('api/coupons/', include(('coupon.urls', 'coupon'), namespace='coupon')),
    path('api/doubts/', include('doubt.urls')),
    path('api/orders/', include('order.urls')),
    path('api/reviews/', include('review.urls')),

]
