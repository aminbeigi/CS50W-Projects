from django.urls import include, path

from . import views

urlpatterns = [
    path('wiki/<str:word>', views.content),
    path(r'(?i)search/', views.get_search),
    path('', views.index, name='index')
]
