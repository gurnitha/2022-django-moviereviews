# movie/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals

# Create your views here.

def home(request):
	return HttpResponse('<h1>Welcome to Home Page</h1>')


def about(request):
	return HttpResponse('<h1>Welcome to About Page</h1>')
