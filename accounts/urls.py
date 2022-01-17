# accounts/urls.py

# Django modules
from django.urls import path

# Locals
from accounts import views

app_name = 'accounts'

urlpatterns = [ 
    path('accounts/signupaccount/', views.signupaccount, name='signupaccount'),
]
