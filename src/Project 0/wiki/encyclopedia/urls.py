from django.urls import include, path

from . import views

urlpatterns = [
    path('wiki/<str:word>', views.content),
    path('search/', views.get_search),
    path('', views.index, name='index')
]
