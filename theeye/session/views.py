from rest_framework import generics
from session.models import Session
from session.serializers import SessionSerializer


class SessionView(generics.ListCreateAPIView):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()


class SessionRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = SessionSerializer
    queryset = Session.objects.all()