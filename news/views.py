# news/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals
from news.models import News

# Create your views here.

def news(request):

	newss = News.objects.order_by('-date')
	# newss = News.objects.all()
	
	context = {
		'newss':newss
	}

	return render(request, 'news/news.html', context)