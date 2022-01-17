# movie/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

# Locals
from movie.models import Movie, Review
from movie.forms import ReviewForm

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
	# Using the filter function, we retrieve reviews
	# for a particular movie only.
	reviews = Review.objects.filter(movie = movie)

	# We then pass in reviews to detail.html via context.
	context = {
		'movie':movie,
		'reviews':reviews
	}	

	return render(request, 'movie/detail.html', context)


def createreview(request, movie_id):

	# We first get the movie object from the database.
	movie = get_object_or_404(Movie,pk=movie_id)

	'''
	When we receive a GET request, it means
	that a user is navigating to the create review
	page and we render createreview.html and
	pass in the review form for the user to create
	the review. We will later show how to create
	the Review Form.
	'''
	if request.method == 'GET':
		return render(request, 'movie/createreview.html', {'form':ReviewForm(), 'movie': movie})
	
		'''
		When user submits the createreview form,
		this function will receive a POST request, and
		we enter the else clause.
		'''
	else:
		try:
			# We retrieve the submitted form from the request.
			form = ReviewForm(request.POST)
			'''
			We create and save a new review object from
			the form’s values but do not yet put it into the
			database (commit=False) because we want to
			specify the user and movie relationships for
			the review.
			'''
			newReview = form.save(commit=False)
			'''
			Finally, we specify the user and movie
			relationships for the review and save the
			review into the database. We then redirect the
			user back to the movie’s detail page.
			'''
			newReview.user = request.user
			newReview.movie = movie
			newReview.save()

			return redirect('movie:detail', newReview.movie.id)

			'''
			If there’s any error with the passed-in data,
			we render createreview.html again and pass
			in an error message.
			'''
		except ValueError:
			return render(request, 'movie/createreview.html', {'form':ReviewForm(),'error':'bad data passedin'})