from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from event.filter import EventFilter
from event.models import Event
from event.serializers import EventSerializer
from event.tasks import eventCreate

class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter
    ordering = ['-timestamp']

    def post(self, request, *args, **kwargs):
        eventCreate.delay(request.data, request.user.id)
        return Response(status=status.HTTP_200_OK)
        # return self.create(request, *args, **kwargs)


class EventRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = EventSerializer
    queryset = Event.objects.all()
