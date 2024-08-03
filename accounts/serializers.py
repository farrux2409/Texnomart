from rest_framework import serializers
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'])
        # user = User.objects.create_superuser(validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user