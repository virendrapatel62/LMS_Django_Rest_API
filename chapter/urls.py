from chapter.views import chapter_types_view, video_plateform_view
from django.contrib import admin
from django.urls import path
# base url : api/chapters/
urlpatterns = [
    path('chapter-types/', chapter_types_view, name='chapter-type-view'),

    path('video-plateforms/', video_plateform_view,
         name='video-plateform-listview'),
]
