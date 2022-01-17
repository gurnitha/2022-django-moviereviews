# movie/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='movie/images/')
	url = models.URLField(blank=True)

	def __str__(self):
		return self.title


class Review(models.Model):
	text = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)
	'''
	For the user and movie field, we are using a
	ForeignKey which allows for a many-to-one
	relationship. This means that a user can create
	multiple reviews. A movie similarly can have
	multiple reviews.

	For user, the reference is to the built-in User
	model that Django provides for
	authentication. 
	'''
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
	'''
	Lastly, we have a boolean property
	watchAgain for users to indicate if they will
	watch the movie again.
	'''
	watchAgain = models.BooleanField()

	def __str__(self):
		return self.text
