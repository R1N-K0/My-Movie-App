from django.shortcuts import render
from .services import get_popular_movies

# Create your views here.
def home(request):
    popular_movies = get_popular_movies()

    return render(request, "movies/home.html", {"popular_movies": popular_movies})