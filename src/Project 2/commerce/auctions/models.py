from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

"""
test_user
cY4jmdE0
"""

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)