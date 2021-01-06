from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

'''
John
asdfasdf234
'''

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    image = models.ImageField(default='default.jpg', upload_to='images', blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'comment by {self.author.username}'

"""
class Bid(models.Model):
    bid = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"the bid of {self.listing}"
"""