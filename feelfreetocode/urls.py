
from order.models import Order
from django.contrib import admin
from django.urls import path, include
from core.views import api_root, MyTokenObtainPairView
from order.urls import Orderurls, subscriptionUrls


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/', api_root, name='api_root'),

    path('api/', include(('course.urls', 'course'), namespace='course')),

    path('api/chapters/', include(('chapter.urls', 'chapter'), namespace='chapter')),
    path('api/coupons/', include(('coupon.urls', 'coupon'), namespace='coupon')),
    path('api/doubts/', include(('doubt.urls', 'doubt'), namespace='doubt')),
    path('api/orders/', include((Orderurls, 'order'), namespace='order')),
    path('api/subscriptions/',
         include((subscriptionUrls, 'order'), namespace='subscription')),
    path('api/reviews/', include(('review.urls', 'review'), namespace='review')),


    # authentication Token Views
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
