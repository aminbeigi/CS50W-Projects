from django.urls import include, path, re_path

from . import views

urlpatterns = [
    #path('wiki/<str:word>', views.content),
    re_path(r'^wiki/(?P<word>\w+)$(?i)', views.content),    
    path('wiki/search/', views.get_search),
    path('wiki/random/', views.random_page, name='random'),
    path('wiki/create-new-page/', views.create_new_page, name='create_new_page'),
    path('', views.index, name='index')
]
