from rest_framework import serializers

from userData.models import userData


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ('firstName', 'lastName', 'Email', 'userName',
                  'DOB', 'contactNumber', 'password')
