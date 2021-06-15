from django.db.models import fields
from doubt.models import Doubt, DoubtAnswer
from rest_framework.serializers import ModelSerializer


class DoubtSerializer(ModelSerializer):
    class Meta:
        model = Doubt
        fields = '__all__'


class DoubtAnswerSerializer(ModelSerializer):
    class Meta:
        model = DoubtAnswer
        fields = '__all__'
