from django.contrib.auth.models import User
from django.db.models import fields
from doubt.models import Doubt, DoubtAnswer
from rest_framework.serializers import ModelSerializer
from core.serializers import UserSerializer


class DoubtSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Doubt
        fields = '__all__'

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        request = self.context['request']
        validated_data['user'] = request.user
        return validated_data


class DoubtAnswerSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = DoubtAnswer
        fields = '__all__'

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        request = self.context['request']
        validated_data['user'] = request.user
        return validated_data
