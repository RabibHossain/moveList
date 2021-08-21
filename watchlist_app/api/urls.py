from django.urls import path, include
# from watchlist_app.api.views import movie_lists, movie_details
from watchlist_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    # path('list/', movie_lists, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-detail'),

    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
    
]
