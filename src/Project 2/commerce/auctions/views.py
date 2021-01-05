from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import User, Listing
from .forms import CreateListing

def index(request):
    return render(request, "auctions/index.html", {
        'Listing': Listing.objects.all()
    })

def listing(request, id):
    return render(request, "auctions/listing.html", {
        'listing': Listing.objects.get(id=id)
    })

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = CreateListing(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = request.user
            listing.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Created new listing for {title}.')
            return redirect('/')
    else:
        form = CreateListing()
    return render(request, 'auctions/create_listing.html', {
        'form': form
        })

def login_redirect(request):
    messages.error(request, 'You need to be signed in to view this page.')
    return redirect('/login')