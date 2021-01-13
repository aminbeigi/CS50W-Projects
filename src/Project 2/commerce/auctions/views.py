from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Comment
from .forms import CreateListing, CreateComment, CreateBid

def index(request):
    return render(request, "auctions/index.html", {
        'Listing': Listing.objects.all()
    })

def listing(request, id):
    if request.method == 'POST' and 'comment-form' in request.POST:
        if str(request.user) == 'AnonymousUser':
            messages.error(request, f'You need to be signed in to comment.')
            return redirect(f'/listing/{id}')
        comment_form = CreateComment(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.listing = Listing.objects.get(id=id)
            comment.save()
            messages.success(request, f'Created new comment.')
            return redirect(f'/listing/{id}')
    if request.method == 'POST' and 'bid-form' in request.POST:
        if str(request.user) == 'AnonymousUser':
            messages.error(request, f'You need to be signed in to bid.')
            return redirect(f'/listing/{id}')
        bid_form = CreateBid(request.POST)
        if bid_form.is_valid():
            bid = bid_form.save(commit=False)
            bid.author = request.user
            bid.listing = Listing.objects.get(id=id)
            bid.save()
            messages.success(request, f'Placed bid of ${bid.price} on {bid.listing.title}.')
            return redirect(f'/listing/{id}')
    else:
        comment_form = CreateComment()
        bid_form = CreateBid()
    return render(request, "auctions/listing.html", {
        'listing': Listing.objects.get(id=id),
        'comments': Comment.objects.all(), #TODO this doesn't need to be here
        'comment_form': comment_form,
        'bid_form': bid_form,
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
            return redirect(f'/listing/{listing.id}')
    else:
        form = CreateListing()
    return render(request, 'auctions/create_listing.html', {
        'form': form
        })

def login_redirect(request):
    messages.error(request, 'You need to be signed in to view this page.')
    return redirect('/login')