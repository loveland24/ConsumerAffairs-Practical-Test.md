from rest_framework import serializers
from session.models import Session
from user.models import User
from user.serializers import UserSerializer
from django.db import transaction

class SessionSerializer(serializers.ModelSerializer):
    application = UserSerializer(read_only=True)

    class Meta:
        model = Session
        fields = '__all__'

    def create(self, validated_data):
        with transaction.atomic():
            request = self.context.get('request')
            validated_data['application'] = request.user
            new_session = super().create(validated_data)
            return new_session
