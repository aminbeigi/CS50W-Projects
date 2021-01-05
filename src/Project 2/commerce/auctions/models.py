from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    image = models.ImageField(default='default.jpg', upload_to='images', blank=True)

    def __str__(self):
        return f'{self.title}'