from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getMovie/<str:category>/',
         views.getMoviesByCategory,
         name='getMoviesByCategory'),
]