# accounts/urls.py

# Django modules
from django.urls import path

# Locals
from accounts import views

app_name = 'accounts'

urlpatterns = [ 
    path('accounts/signupaccount/', views.signupaccount, name='signupaccount'),
    path('accounts/logout/', views.logoutaccount, name='logoutaccount'),
    path('accounts/login/', views.loginaccount, name='loginaccount'),
]
