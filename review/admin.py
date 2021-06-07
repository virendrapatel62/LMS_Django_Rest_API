from django.contrib import admin
from review.models import Review
# Register your models here.


class ReviewAdminModel(admin.ModelAdmin):
    model = Review
    list_display = ['course', 'rating', 'user']


admin.site.register(Review, ReviewAdminModel)
