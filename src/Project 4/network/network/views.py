import json
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post

@csrf_exempt
def posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        # return posts in reverse chronologial order
        posts = posts.order_by('-timestamp').all()
        return JsonResponse([post.serialize() for post in posts], safe=False)

    # creating a new post must be via POST
    if request.method == 'POST':
        data = json.loads(request.body)

        # get user object from username 
        username = data.get('user', '') # if user doesn't exist return ''
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({
                'error': f'User with post {post} does not exist.'
            }, status=400)

        # get contents of post
        title = data.get('title', '')
        body = data.get('body', '')

        # create and save Post object
        new_post = Post()
        new_post.title = title
        new_post.body = body
        new_post.user = user
        new_post.save()

        return JsonResponse({'message': "Post sent successfully."}, status=201)

    # sent other request
    return JsonResponse({'error': "GET or POST request required."}, status=400)

@csrf_exempt
def post(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return JsonResponse(post.serialize())

    if request.method == 'DELETE':
        post = Post.objects.get(id=post_id)
        post.delete()
        return JsonResponse({'message': "Delete sent successfully."}, status=200)

    # sent other request
    return JsonResponse({'error': "GET or DELETE request required."}, status=400)