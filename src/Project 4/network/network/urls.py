from django.urls import path, re_path

from . import views

urlpatterns = [
   # API Routes
    path("posts", views.posts),
    path("posts/<int:post_id>", views.post),
]