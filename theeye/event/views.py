from rest_framework import generics
from event.models import Event
from event.serializers import EventSerializer


class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = EventSerializer
    queryset = Event.objects.all()
