from django.urls import path

from . import views

urlpatterns = [
   # API Routes
    path("posts", views.posts),
    #path("emails/<int:email_id>", views.email, name="email"),
]