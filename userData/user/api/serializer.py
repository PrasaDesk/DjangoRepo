from rest_framework import serializers
from user.models import User_data
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher, make_password
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserDataSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = User_data
        fields = ('id', 'user', 'phone', 'city', 'bio',
                  'sequrity_que', 'sequrity_ans')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of USER
        :return: returns a successfully created USER record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        user.password = make_password(user.password)
        user.save()
        USER, created = User_data.objects.update_or_create(user=user,
                                                           phone=validated_data.pop(
                                                               'phone'),
                                                           city=validated_data.pop(
                                                               'city'),
                                                           bio=validated_data.pop(
                                                               'bio'),
                                                           sequrity_que=validated_data.pop(
                                                               'sequrity_que'),
                                                           sequrity_ans=validated_data.pop('sequrity_ans'))

        return USER
