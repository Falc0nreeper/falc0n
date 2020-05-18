from django.shortcuts import render
from .models import Movie
from django.views.generic.base import View
# Create your views here.

class MoviesView(View):

    def get (self, request):
        movies = Movie.objects.all()
        return render (request, 'movies/movielist.html', {'movie_list': movies})

class MovieDetailView(View):

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "movies/moviesingle.html", {'movie': movie})
