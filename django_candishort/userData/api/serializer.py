from rest_framework import serializers

from userData.models import userData


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ('id', 'firstname', 'lastname', 'email', 'username', 'gender',
                  'dob', 'password', 'contactno', 'security_question', 'security_answer')


class userSerializerLogin(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ('username', 'password')
