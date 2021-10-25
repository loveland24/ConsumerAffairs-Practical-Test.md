from django.db import models
from django.utils import timezone

class Event(models.Model):
    session = models.ForeignKey('session.Session', on_delete=models.CASCADE, related_name='events')
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=1500)
    timestamp = models.DateTimeField(default=timezone.now)
