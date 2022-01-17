# movie/admin.py

# Django module
from django.contrib import admin

# Locals
from movie.models import Movie, Review

# Register your models here.

admin.site.register(Movie)
admin.site.register(Review)

