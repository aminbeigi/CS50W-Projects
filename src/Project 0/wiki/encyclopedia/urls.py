from django.urls import include, path, re_path

from . import views

urlpatterns = [
    #path('wiki/<str:word>', views.content),
    re_path(r'^(?i)wiki/(?P<word>\w+)$', views.content),    
    path('search/', views.get_search),
    path('', views.index, name='index')
]
