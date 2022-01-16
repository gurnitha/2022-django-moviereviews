# movie/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals

# Create your views here.

def home(request):
	return render(request, 'movie/home.html', {'name':'Greg Lim'})


def about(request):
	return render(request, 'movie/about.html', {'name':'Movie Review'})
