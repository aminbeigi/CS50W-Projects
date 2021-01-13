from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Comment
from .models import categories as categories_tuple
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
            if (bid.author.username == bid.listing.author.username):
                messages.error(request, f"You can not bid on your own listing.")
                return redirect(f'/listing/{id}')
            if (bid.price <= bid.listing.price):
                messages.error(request, f"Bid of ${bid.price} is lower than listing price of ${bid.listing.price}.")
                return redirect(f'/listing/{id}')
            bid.save()
            messages.success(request, f"Placed bid of ${bid.price} on {bid.listing.title}.")
            return redirect(f'/listing/{id}')
    else:
        comment_form = CreateComment()
        bid_form = CreateBid()
    return render(request, "auctions/listing.html", {
        'listing': Listing.objects.get(id=id),
        'comment_form': comment_form,
        'bid_form': bid_form,
    })

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = CreateListing(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            listing = form.save(commit=False)
            listing.author = request.user
            listing.save()
            messages.success(request, f'Created new listing for {listing.title}.')
            return redirect(f'/listing/{listing.id}')
    else:
        form = CreateListing()
    return render(request, 'auctions/create_listing.html', {
        'form': form
        })

def categories(request):
    categories_lst = []
    for category in categories_tuple:
        print(category)
        categories_lst.append(category[0])

    return render(request, 'auctions/categories.html', {
        'Listing': Listing,
        'categories': categories_lst
        })

def display_categories(request, category):
    categories_lst = []
    for category in categories_tuple:
        print(category)
        categories_lst.append(category[0])

    return render(request, 'auctions/categories.html', {
        'Listing': Listing,
        'categories': categories_lst
        })

def login_redirect(request):
    messages.error(request, 'You need to be signed in to view this page.')
    return redirect('/login')