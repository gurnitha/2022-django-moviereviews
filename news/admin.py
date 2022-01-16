# news/admin.py

# Django module
from django.contrib import admin

# Locals
from news.models import News

# Register your models here.

admin.site.register(News)

