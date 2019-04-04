from rest_framework import serializers
from user.models import User_data
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserDataSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False, many=False)

    class Meta:
        model = User_data
        fields = ('id', 'user', 'phone', 'city', 'bio',
                  'sequrity_que', 'sequrity_ans')
