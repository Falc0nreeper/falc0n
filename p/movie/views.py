from django.shortcuts import render
from .models import Movie
from django.views.generic.base import View
# Create your views here.

class MoviesView(View):

    def get (self, request):
        movies = Movie.objects.all()
        return render (request, 'movies/movielist.html', {'movie_list': movies})