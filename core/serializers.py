from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_admin'] = user.is_superuser
        token['username'] = user.username
        # ...

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', "last_name",
                  'email', 'username', 'is_superuser']
