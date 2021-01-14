from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from decimal import Decimal

'''
John
asdfasdf234
'''

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=25)
    slug_name = models.CharField(max_length=25)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.01'))])
    image = models.ImageField(default='default.jpg', upload_to='images', blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    comment = models.TextField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default=None, related_name='comments')

    def __str__(self):
        return f"comment by {self.author.username} in {self.listing.title}"

class Bid(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.01'))])

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"bid by {self.listing} by {self.author.username} @ ${self.price}"

class Watchlist(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listings")
    # Watchlist('bob', 'Broom')
    # Watchlist('bob', 'Cat')

    def __str__(self):
        return f"watchlist of {self.author.username}"