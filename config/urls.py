# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include


urlpatterns = [ 

    # Admin
    path('admin/', admin.site.urls),

    # Movie
    path('', include('movie.urls', namespace='movie'))
]
