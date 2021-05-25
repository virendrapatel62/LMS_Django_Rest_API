from django.contrib import admin
from .models import Course, Category, Tag
# Register your models here.

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Tag)
