from typing import Text
from django.db import models
from course.models import Course
import uuid
# Create your models here.

chapter_choises = (
    ('T', 'TEXT'),
    ('H', 'HEADING'),
    ('V', 'VIDEO'),
    ('L', 'LINK')
)
chapter_choises_description = (
    ('T', 'Create your textual lessons in the course. It can also be used to embed iFrame, add HTML code through the Source option'),
    ('H', 'Define your chapter or section headings.'),
    ('V', 'All uploaded videos are completely secure and non downloadable. It can also be used to embed youtube and Vimeo videos.'),
    ('L', 'Add Link which will be embedded in iFrame')
)

video_plateform_choises = (
    ('Y', 'Youtube'),
    ('V', 'Vimeo')
)


class Chapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='chapters')
    chapter_type = models.CharField(choices=chapter_choises, max_length=2)
    index = models.IntegerField(null=False)
    parent_chapter = models.ForeignKey('Chapter', null=True, blank=True,
                                       on_delete=models.CASCADE, related_name='child_chapters')


class LinkChapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    lecture = models.OneToOneField(
        Chapter, on_delete=models.CASCADE, related_name='link_chapter')
    title = models.CharField(max_length=30)
    url = models.URLField(max_length=100)


class HeadingChapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    lecture = models.OneToOneField(
        Chapter, on_delete=models.CASCADE, related_name='heading_chapter')
    title = models.CharField(max_length=30)


class TextChapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    lecture = models.OneToOneField(
        Chapter, on_delete=models.CASCADE, related_name='text_chapter')
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=10000)


class VideoChapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    lecture = models.OneToOneField(
        Chapter, on_delete=models.CASCADE, related_name='video_chapter')
    title = models.CharField(max_length=30)
    video_id = models.CharField(max_length=30, unique=False)
    description = models.CharField(max_length=10000)
    video_plateform = models.CharField(
        choices=video_plateform_choises, max_length=2)
