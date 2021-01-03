from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import User, Listing


def index(request):
    return render(request, "auctions/index.html", {
        'Listing': Listing.objects.all()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect("index") 
        else:
            messages.error(request, f"Invalid username and/or password.") 
            return render(request, "auctions/login.html")
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return redirect("index") 