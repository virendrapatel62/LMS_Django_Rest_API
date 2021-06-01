from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from chapter.models import Chapter, TextChapter, VideoChapter, LinkChapter, HeadingChapter
from rest_framework.serializers import ModelSerializer


class TextChapterSerializer(ModelSerializer):
    chapter = serializers.UUIDField(required=False)

    class Meta:
        model = TextChapter
        fields = '__all__'


class HeadingChapterSerializer(ModelSerializer):
    chapter = serializers.UUIDField(required=False)

    class Meta:
        model = HeadingChapter
        fields = '__all__'


class VideoChapterSerializer(ModelSerializer):
    chapter = serializers.UUIDField(required=False)

    class Meta:
        model = VideoChapter
        fields = '__all__'


class LinkChapterSerializer(ModelSerializer):
    chapter = serializers.UUIDField(required=False)

    class Meta:
        model = LinkChapter
        fields = '__all__'


class ChapterSerializer(ModelSerializer):
    index = serializers.IntegerField(required=False)

    class Meta:
        model = Chapter
        fields = '__all__'

    def create(self, validated_data):
        data = self.context.get('request').data
        chapter_type = data.get('chapter_type')
        chapter_type_object = None

        if(chapter_type == 'H'):
            chapter_type_object = self.handleHeadingChapter(data)

        if(chapter_type == 'T'):
            chapter_type_object = self.handleTextChapter(data)

        if(chapter_type == 'L'):
            chapter_type_object = self.handleLinkChapter(data)

        if(chapter_type == 'V'):
            chapter_type_object = self.handleVideoChapter(data)

        print("validated Data : CHapter Data", validated_data)

        chapter = Chapter(**validated_data)
        course = chapter.course

        if(chapter.parent_chapter is None):
            last_index_parent_chapter = Chapter.objects.filter(
                course=course, parent_chapter=None).count()
            chapter.index = last_index_parent_chapter + 1
            chapter.save()
            chapter_type_object.chapter = chapter
            chapter_type_object.save()
        else:
            # find index of child chapter
            pass

        return chapter

    def handleHeadingChapter(self, raw_json):
        heading_chapter_raw = raw_json.get('heading_chapter')
        if not heading_chapter_raw:
            raise ValidationError(
                {"heading_chapter": ["heading_chapter is required"]})

        header_chapter_serializer = HeadingChapterSerializer(
            data=heading_chapter_raw)

        if header_chapter_serializer.is_valid():
            return HeadingChapter(**header_chapter_serializer._validated_data)
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
            return TextChapter(**text_chapter_serializer._validated_data)
        else:
            raise ValidationError(
                {"text_chapter": text_chapter_serializer.errors})

    def handleLinkChapter(self, raw_json):
        link_chapter_raw = raw_json.get('link_chapter')
        if not link_chapter_raw:
            raise ValidationError(
                {"link_chapter": ["link_chapter is required"]})

        link_chapter_serializer = LinkChapterSerializer(
            data=link_chapter_raw)

        if link_chapter_serializer.is_valid():
            return LinkChapter(**link_chapter_serializer._validated_data)
        else:
            raise ValidationError(
                {"link_chapter": link_chapter_serializer.errors})

    def handleVideoChapter(self, raw_json):
        video_chapter_raw = raw_json.get('video_chapter')
        if not video_chapter_raw:
            raise ValidationError(
                {"video_chapter": ["video_chapter is required"]})

        video_chapter_serializer = VideoChapterSerializer(
            data=video_chapter_raw)

        if video_chapter_serializer.is_valid():
            return VideoChapter(**video_chapter_serializer._validated_data)
        else:
            raise ValidationError(
                {"video_chapter": video_chapter_serializer.errors})
