from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing/<int:id>', views.listing, name='listing'),
    path('listing/create-listing', views.create_listing, name='create_listing'),
    path('accounts/login/', views.login_redirect)
]
