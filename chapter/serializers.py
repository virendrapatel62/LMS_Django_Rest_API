from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from chapter.models import Chapter, TextChapter, VideoChapter, LinkChapter, HeadingChapter
from rest_framework.serializers import ModelSerializer


class TextChapterSerializer(ModelSerializer):
    lecture = serializers.UUIDField(required=False)

    class Meta:
        model = TextChapter
        fields = '__all__'


class HeadingChapterSerializer(ModelSerializer):
    lecture = serializers.UUIDField(required=False)

    class Meta:
        model = HeadingChapter
        fields = '__all__'


class VideoChapterSerializer(ModelSerializer):
    lecture = serializers.UUIDField(required=False)

    class Meta:
        model = VideoChapter
        fields = '__all__'


class LinkChapterSerializer(ModelSerializer):
    lecture = serializers.UUIDField(required=False)

    class Meta:
        model = LinkChapter
        fields = '__all__'


class ChapterSerializer(ModelSerializer):
    index = serializers.IntegerField(required=False)

    class Meta:
        model = Chapter
        fields = '__all__'

    def create(self, validated_data):
        print('********************')
        print('inside create method')
        print('validated_data :', validated_data)
        print("request.data : ", self.context.get('request').data)
        data = self.context.get('request').data
        chapter_type = data.get('chapter_type')
        if(chapter_type == 'H'):
            self.handleHeadingChapter(data)

        if(chapter_type == 'T'):
            self.handleTextChapter(data)

        return Chapter()

    def handleHeadingChapter(self, raw_json):
        heading_chapter_raw = raw_json.get('heading_chapter')
        if not heading_chapter_raw:
            raise ValidationError(
                {"heading_chapter": ["heading_chapter is required"]})

        header_chapter_serializer = HeadingChapterSerializer(
            data=heading_chapter_raw)

        if header_chapter_serializer.is_valid():
            print(header_chapter_serializer.validated_data)
        else:
            raise ValidationError(
                {"heading_chapter": header_chapter_serializer.errors})

    def handleTextChapter(self, raw_json):
        text_chapter_raw = raw_json.get('text_chapter')
        if not text_chapter_raw:
            raise ValidationError(
                {"text_chapter": ["text_chapter is required"]})

        text_chapter_serializer = TextChapterSerializer(
            data=text_chapter_raw)

        if text_chapter_serializer.is_valid():
            print(text_chapter_serializer.validated_data)
        else:
            raise ValidationError(
                {"text_chapter": text_chapter_serializer.errors})
