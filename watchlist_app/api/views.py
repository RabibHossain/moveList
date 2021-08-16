from django.http import response
from rest_framework.response import Response
from watchlist_app.api.serializers import MovieSerializer
from django.http.response import JsonResponse
from django.shortcuts import render
from watchlist_app.models import Movie
from rest_framework.decorators import api_view

 
@api_view()
def movie_lists(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)

@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)

    return Response(serializer.data)