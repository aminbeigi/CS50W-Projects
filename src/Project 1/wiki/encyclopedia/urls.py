from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('wiki/<str:title>', views.content),
    path('wiki/<str:title>/edit-entry', views.edit_entry, name='edit_entry'),  
    path('wiki/search/', views.get_search),
    path('wiki/random/', views.random_page, name='random'),
    path('wiki/create-new-page/', views.create_new_page, name='create_new_page'),
    path('', views.index, name='index')
]
