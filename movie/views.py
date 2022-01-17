# movie/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Locals
from movie.models import Movie

# Create your views here.

def home(request):

	searchTerm = request.GET.get('searchMovie')

	if searchTerm:
		movies = Movie.objects.filter(title__icontains=searchTerm)
	else:
		movies = Movie.objects.all()
		
	context = {
		'searchTerm':searchTerm,
		'movies':movies
	}
	return render(request, 'movie/home.html', context)


def about(request):
	return render(request, 'movie/about.html', {'name':'Movie Review'})


def signup(request):
	email = request.GET.get('email')
	return render(request, 'movie/signup.html', {'email':email})


def detail(request, movie_id):
	movie = get_object_or_404(Movie,pk=movie_id)
	
	context = {
		'movie':movie
	}	

	return render(request, 'movie/detail.html', context)

