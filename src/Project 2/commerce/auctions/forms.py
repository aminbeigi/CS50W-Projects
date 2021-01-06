from django.forms import ModelForm
from auctions.models import Listing, Comment

class CreateListing(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'image']

class CreateComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']