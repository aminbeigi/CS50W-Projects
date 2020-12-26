from django.urls import include, path

from . import views

urlpatterns = [
    path('wiki/<str:word>', views.content),
    path('', views.index, name='index'),
]
