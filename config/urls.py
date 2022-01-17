# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 

    # Admin
    path('admin/', admin.site.urls),

    # Movie
    path('', include('movie.urls', namespace='movie')),

    # News
    path('', include('news.urls', namespace='news')),

    # Accounts
    path('', include('accounts.urls', namespace='accounts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
