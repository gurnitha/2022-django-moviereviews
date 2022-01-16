# news/urls.py

# Django modules
from django.urls import path

# Locals
from news import views

app_name = 'news'

urlpatterns = [ 
    path('news/', views.news, name='news'),
]
