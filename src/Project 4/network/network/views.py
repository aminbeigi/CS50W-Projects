import json
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post

@csrf_exempt
def posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        # Return posts in reverse chronologial order
        posts = posts.order_by("-timestamp").all()
        return JsonResponse([post.serialize() for post in posts], safe=False)