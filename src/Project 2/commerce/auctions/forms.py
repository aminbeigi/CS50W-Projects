from django import forms
from django.forms import ModelForm
from auctions.models import Listing, Comment, Bid, Category

categories = [
    ('gaming', 'Gaming'),
    ('housekeeping', 'Housekeeping'),
    ('other', 'Other')
]

class CreateListing(ModelForm):
    name = forms.ChoiceField(choices=categories, required=False) 

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