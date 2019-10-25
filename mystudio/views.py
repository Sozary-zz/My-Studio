from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Category
from .models import Movie


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def getMoviesByCategory(request,category):
    movie = Movie.objects.filter(category__name=category)
    data={}
    json_data = serializers.serialize("json", movie)
    data["status"]=200
    data["data"]=json_data

    return JsonResponse(data)
