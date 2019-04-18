from rest_framework import serializers
from user.models import User, User_data
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'password', 'first_name', 'last_name')


class UserDataSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = User_data
        fields = ('id', 'user', 'gender', 'dob', 'contactno',
                  'sequrity_que', 'sequrity_ans')

    def create(self, validated_data):
        """
        custome create metthod because we extending the user table using OneToOne relation ship so we 
        need to write own create method
        """
        print("create method call")
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)

        # default model take RawString as Password we need to encrypt and then stored it in database
        user.password = make_password(user.password)
        user.save()

        USER, created = User_data.objects.update_or_create(user=user,
                                                           gender=validated_data.pop(
                                                               'gender'),
                                                           dob=validated_data.pop(
                                                               'dob'),
                                                           contactno=validated_data.pop(
                                                               'contactno'),
                                                           sequrity_que=validated_data.pop(
                                                               'sequrity_que'),
                                                           sequrity_ans=validated_data.pop(
                                                               'sequrity_ans'))

        return USER
