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

def listing(request, id):
    return render(request, "auctions/listing.html", {
        'listing': Listing.objects.get(id=id)
    })