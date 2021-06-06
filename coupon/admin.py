from django.contrib import admin
from coupon.models import Coupon
# Register your models here.


class CouponAdminModel(admin.ModelAdmin):
    model = Coupon
    list_display = ['code', 'course', 'discount', 'active']


admin.site.register(Coupon, CouponAdminModel)
