from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing/<int:id>', views.listing, name='listing')
]
