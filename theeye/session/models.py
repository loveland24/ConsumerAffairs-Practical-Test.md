from django.db import models

# Create your models here.
class Session(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    application = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='applications')