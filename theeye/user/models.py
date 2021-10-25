from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    application_name = models.CharField(max_length=150)
