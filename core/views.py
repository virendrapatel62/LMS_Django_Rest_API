from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request):
    response = {
        "API Root": reverse('api_root', request=request),

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
            "Chapter CReate": reverse('chapter:createview', request=request),
        }


    }
    return Response(response)
