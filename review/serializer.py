from django.db.models import fields
from review.models import Review
from rest_framework.serializers import ModelSerializer
from course.serializers import Course, CourseSerializer
from core.serializers import User, UserSerializer


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

    def to_representation(self, instance):
        json = super().to_representation(instance)
        course = Course.objects.get(pk=json.get('course'))
        course_json = CourseSerializer(course, context=self.context).data

        user = User.objects.get(pk=json.get('user'))
        user_json = UserSerializer(user, context=self.context).data

        json['course'] = course_json
        json['user'] = user_json
        return json
