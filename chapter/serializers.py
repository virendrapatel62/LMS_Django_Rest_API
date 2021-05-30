from django.db.models import fields
from chapter.models import Chapter, TextChapter, VideoChapter, LinkChapter, HeadingChapter
from rest_framework.serializers import ModelSerializer


class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class TextChapterSerializer(ModelSerializer):
    class Meta:
        model = TextChapter
        fields = '__all__'


class HeadingChapterSerializer(ModelSerializer):
    class Meta:
        model = HeadingChapter
        fields = '__all__'


class VideoChapterSerializer(ModelSerializer):
    class Meta:
        model = VideoChapter
        fields = '__all__'


class LinkChapterSerializer(ModelSerializer):
    class Meta:
        model = LinkChapter
        fields = '__all__'
