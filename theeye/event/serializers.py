from django.utils import timezone
from rest_framework import serializers

from event.models import Event
from session.models import Session
from session.serializers import SessionSerializer
from django.db import transaction
import json


class EventSerializer(serializers.ModelSerializer):
    session = SessionSerializer(read_only=True)
    session_id = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Event
        fields = '__all__'

    def validate_timestamp(self, value):
        if value > timezone.now():
            raise serializers.ValidationError({'Timestamp': 'Cannot be in the future'})
        return value

    def to_internal_value(self, data):
        data['data'] = json.dumps(data.pop('data'))
        return super().to_internal_value(data)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['data'] = json.loads(response['data'])
        return response

    def validate(self, data):
        self._validate_payload(data)
        return data

    def create(self, validated_data):
        application_id = self.context.get('application_id')
        session_id = validated_data.pop('session_id')
        with transaction.atomic():
            session, create = Session.objects.get_or_create(id=session_id, application_id=application_id)
            validated_data['session'] = session
            new_event = super().create(validated_data)
            return new_event

    def _validate_payload(self, data):
        identity = '{}-{}'.format(data['data'], data['name'])
        if identity == 'page interaction-pageview':
            #add validation for this event
            pass
        elif identity == 'page interaction-cta click':
            # add validation for this event
            pass
        elif identity == 'form interaction-submit':
            # add validation for this event
            pass