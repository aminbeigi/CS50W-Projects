from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Comment, Category, Watchlist
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
            bid.user = request.user
            bid.listing = Listing.objects.get(id=id)
            if (bid.user.username == bid.listing.author.username):
                messages.error(request, f"You can not bid on your own listing.")
                return redirect(f'/listing/{id}')
            if (bid.price <= bid.listing.price):
                messages.error(request, f"Bid of ${bid.price} is lower than listing price of ${bid.listing.price}.")
                return redirect(f'/listing/{id}')
            bid.save()
            messages.success(request, f"Placed bid of ${bid.price} on {bid.listing.title}.")
            return redirect(f'/listing/{id}')
    if request.method == 'POST' and 'add-watchlist-form' in request.POST:
        if str(request.user) == 'AnonymousUser':
            messages.error(request, f'You need to be signed in to use the watchlist.')
            return redirect(f'/listing/{id}')
        listing = Listing.objects.get(id=id)
        w = Watchlist(user=request.user, listing=listing)
        w.save()
        messages.success(request, f'Added to watchlist.')
        return redirect(f'/listing/{id}')
        
    if request.method == 'POST' and 'remove-watchlist-form' in request.POST:
        listing = Listing.objects.get(id=id)
        w = Watchlist.objects.get(user=request.user, listing=listing)
        w.delete()
        messages.success(request, f'Removed from watchlist.')
        return redirect(f'/listing/{id}')
    else:
        comment_form = CreateComment()
        bid_form = CreateBid()
    return render(request, "auctions/listing.html", {
        'listing': Listing.objects.get(id=id),
        'comment_form': comment_form,
        'bid_form': bid_form,
        'user': request.user
    })

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = CreateListing(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            listing = form.save(commit=False)
            listing.category = Category.objects.filter(slug_name=name)[0]
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
    for category in Category.objects.all():
        categories_lst.append(category)
        #print(Listing.objects.filter(category=category)[-1:0])

    return render(request, 'auctions/categories.html', {
        'categories': categories_lst
        })

def display_category(request, category_name):
    categories_lst = []
    for category in Listing.objects.filter(category__slug_name__contains=category_name):
        categories_lst.append(category)

    return render(request, 'auctions/category_display.html', {
        'Listing': categories_lst,
        'category_name': category_name
        })

def user_profile(request, user):
    profile_page_user = User.objects.get(username=user)
    
    return render(request, 'auctions/user_profile.html', {
        'profile_page_user': profile_page_user
        })

@login_required
def watchlist(request):
    watchlist_lst = []

    for watchlist_item in Watchlist.objects.filter(user__username__contains=str(request.user)):
        watchlist_lst.append(watchlist_item.listing)

    return render(request, 'auctions/watchlist.html', {
        'Listing': watchlist_lst,
        'watchlist_user': str(request.user)
        })

def login_redirect(request):
    messages.error(request, 'You need to be signed in to view this page.')
    return redirect('/login')