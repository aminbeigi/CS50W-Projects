from django import forms
from django.forms import ModelForm
from auctions.models import Listing, Comment, Bid, Category

categories = (
    ('gaming', 'Gaming'),
    ('housekeeping', 'Housekeeping'),
    ('other', 'Other')
)
choices = Category.objects.all().values_list('category', 'category_slug')

class CreateListing(ModelForm):
    category = forms.MultipleChoiceField(choices=categories) 

    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'image', 'category']

class CreateComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class CreateBid(ModelForm):
    class Meta:
        model = Bid
        fields = ['price']