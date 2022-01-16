# 2022-django-moviereviews
My exercise based on Beginning Django 3 Development by Greg Lim


#### 1. Introduction


        The App We Will Be Building

        We will build a Movie reviews app which lets
        users to:
        -	View and search for movies. 
        -	They can also log in and post reviews on the movies
        -	Users can see the list of reviews in a
	        Movie ’ s page and post/edit/delete their own
	        review if they are logged in. 
        -	They will not be able edit/delete other ’ s reviews though.

        Through this app, we will learn a lot of
        concepts like forms, user authorization,
        permissions, foreign keys and more. By the
        end of this book, you will be confident
        creating your own Django projects.


#### 2. Create Django Project


        1. Install and check Python

        - 	python --vesion

        2. Create and activate virtualenv

        - python -m venv venv39327

        3. Installing Django

        - pip install django==3.2.7

        4. Creating Django Project

        - django-admin startproject config .

        5. Run server to test

        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 3. Understanding the project structure

        E:.
        │   .gitignore
        │   LICENSE
        │   manage.py
        │   README.md
        │
        └───config
                asgi.py
                settings.py
                urls.py
                wsgi.py
                __init__.py

