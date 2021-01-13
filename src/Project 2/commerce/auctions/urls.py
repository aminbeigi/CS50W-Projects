from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing/<int:id>', views.listing, name='listing'),
    path('listing/create-listing', views.create_listing, name='create_listing'),
    path('listing/categories', views.categories, name='categories'),
    path('listing/categories/<str:category_name>', views.display_category, name='display_category'),
    path('accounts/login/', views.login_redirect)
]
