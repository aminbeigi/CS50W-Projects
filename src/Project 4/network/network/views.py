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
        # return posts in reverse chronologial order
        posts = posts.order_by("-timestamp").all()
        return JsonResponse([post.serialize() for post in posts], safe=False)

@csrf_exempt
def create_post(request):
    # creating a new post must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)

    # get user object from username 
    username = data.get("user", "") # if user doesn't exist return ""
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({
            "error": f"User with post {post} does not exist."
        }, status=400)

    # get contents of post
    title = data.get("title", "")
    body = data.get("body", "")

    # create and save Post object
    new_post = Post()
    new_post.title = title
    new_post.body = body
    new_post.user = user
    new_post.save()

    return JsonResponse({"message": "Post sent successfully."}, status=201)