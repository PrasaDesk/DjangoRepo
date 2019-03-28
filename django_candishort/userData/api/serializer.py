from rest_framework import serializers

from userData.models import userData


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ('firstname', 'lastname', 'email', 'username', 'gender',
                  'dob', 'contactno', 'password', 'security_question', 'security_answer')
        print(fields[0])
