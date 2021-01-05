from django.forms import ModelForm
from auctions.models import Listing

class CreateListing(ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'image']