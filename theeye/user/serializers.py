from rest_framework import serializers
from user.models import (User)
from django.db import transaction
from django.utils.crypto import get_random_string
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = User
        read_only_fields = ['date_joined', 'last_login']
        exclude = ['id', 'username', 'email', 'last_login', 'date_joined', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions']

    def create(self, validated_data):
        with transaction.atomic():
            validated_data['username'] = get_random_string()
            validated_data['password'] = get_random_string()
            user = User.objects.create_user(**validated_data)
            user.save()
            Token.objects.create(user=user)
            return user
