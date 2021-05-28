from chapter.models import TextChapter, VideoChapter
from django.forms import ModelForm, CharField, Textarea, fields


class TextChapterForm(ModelForm):
    content = CharField(widget=Textarea)

    class Meta:
        model = TextChapter
        fields = '__all__'


class VideoChapterForm(ModelForm):
    description = CharField(widget=Textarea)

    class Meta:
        model = VideoChapter
        fields = '__all__'
