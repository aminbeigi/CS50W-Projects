from django.forms import ModelForm
from auctions.models import Listing, Comment, Bid

class CreateListing(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'image']

class CreateComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class CreateBid(ModelForm):
    class Meta:
        model = Bid
        fields = ['price']