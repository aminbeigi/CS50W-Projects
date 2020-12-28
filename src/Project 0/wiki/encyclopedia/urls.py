from django.urls import include, path, re_path

from . import views

urlpatterns = [
    #path('wiki/<str:word>', views.content),
    re_path(r'^wiki/(?P<word>\w+)$(?i)', views.content),    
    path('search/', views.get_search),
    path('random/', views.random_page, name='random'),
    path('', views.index, name='index')
]
