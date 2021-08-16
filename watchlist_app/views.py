from django.http.response import JsonResponse
from django.shortcuts import render
from watchlist_app.models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }

    return JsonResponse(data)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active,
    }
    print(movie)

    return JsonResponse(data)