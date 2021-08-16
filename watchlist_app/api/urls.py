from django.urls import path, include
from watchlist_app.api.views import movie_lists, movie_details

urlpatterns = [
    path('list/', movie_lists, name='movie-list'),
    path('<int:pk>', movie_details, name='movie-detail'),
    
]
