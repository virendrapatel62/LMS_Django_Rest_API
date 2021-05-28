from chapter.forms import TextChapterForm, VideoChapterForm
from typing import Text
from django.contrib import admin
from django.db.models import fields
from chapter.models import Chapter, LinkChapter, TextChapter, VideoChapter
# Register your models here.


class TextChapterAdminModel(admin.ModelAdmin):
    form = TextChapterForm


class VideoChapterAdminModel(admin.ModelAdmin):
    form = VideoChapterForm


admin.site.register(Chapter)
admin.site.register(LinkChapter)
admin.site.register(TextChapter, TextChapterAdminModel)
admin.site.register(VideoChapter, VideoChapterAdminModel)
