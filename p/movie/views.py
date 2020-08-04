from django.shortcuts import render
from .models import Movie, Category
from django.views.generic.base import View
from .forms import ReviewForm
# Create your views here.

class MoviesView(View):

    def get (self, request):
        movies = Movie.objects.all()
        return render (request, 'movies/movielist.html', {'movie_list': movies})


    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context



class MovieDetailView(View):

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "movies/moviesingle.html", {'movie': movie})

   

class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form_is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())