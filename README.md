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


#### 4. Create the first app 'movie'

        modified:   README.md
        modified:   config/settings.py
        new file:   movie/__init__.py
        new file:   movie/admin.py
        new file:   movie/apps.py
        new file:   movie/migrations/__init__.py
        new file:   movie/models.py
        new file:   movie/tests.py
        new file:   movie/views.py


#### 5. URLs

        modified:   README.md
        modified:   config/urls.py
        new file:   movie/urls.py
        modified:   movie/views.py


#### 6. Generating HTML pages with templates

        new file:   movie/templates/movie/about.html
        new file:   movie/templates/movie/home.html
        modified:   movie/views.py


#### 7. Adding Bootstrap

        modified:   README.md
        modified:   movie/templates/movie/home.html


#### 8. Adding A Search Form


#### 8.1 Retrieving the values submitted

        modified:   README.md
        modified:   movie/templates/movie/home.html
        modified:   movie/views.py


#### 8.2 Sending a Form to Another Page

        modified:   movie/templates/movie/home.html
        new file:   movie/templates/movie/signup.html
        modified:   movie/urls.py
        modified:   movie/views.py


#### 9. Models: Create Movie model

        modified:   README.md
        new file:   movie/migrations/0001_initial.py
        modified:   movie/models.py


#### 10. Django Admin Interface

        Works:

        1. Create superuer
        2. Configuring way to storing the images (MEDIA_ROOT)
        3. Configuring way to handle the media served from MEDIA_ROOT
        4. Serving the Stored Images
        5. Adding Movie model to admin

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   movie/admin.py

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   media/movie/images/gladiator.jpg
        new file:   media/movie/images/limitless.JPG
        new file:   media/movie/images/luther.JPG
        modified:   movie/admin.py


#### 11. DISPLAYING OBJECTSFROM ADMIN

        Works:

        1. Retrieve and display movies form db to the home page
        2. Implementing Search

        modified:   README.md
        modified:   movie/templates/movie/home.html
        modified:   movie/views.py


#### 12. CREATING A NEWS APP

        Works:

        1. Create news app
        2. Create news page
        3. Create News model
        4. Retrieve and display all movies
        5. Filtering retrieve by date of LIFO and display all movies
        6. Add bootstrap to news page

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   news/__init__.py
        new file:   news/admin.py
        new file:   news/apps.py
        new file:   news/migrations/0001_initial.py
        new file:   news/migrations/__init__.py
        new file:   news/models.py
        new file:   news/templates/news/news.html
        new file:   news/tests.py
        new file:   news/urls.py
        new file:   news/views.py


#### 13. Understanding the database

        modified:   README.md

        (moviereviews) λ python manage.py sqlmigrate movie 0001
        BEGIN;
        --
        -- Create model Movie
        --
        CREATE TABLE "movie_movie" (
	        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	        "title" varchar(100) NOT NULL, 
	        "description" varchar(250) NOT NULL, 
	        "image" varchar(100) NOT NULL, 
	        "url" varchar(200) NOT NULL);
        COMMIT;


        (moviereviews) λ python manage.py sqlmigrate news 0001
        BEGIN;
        --
        -- Create model News
        --
        CREATE TABLE "news_news" (
	        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	        "headline" varchar(200) NOT NULL, 
	        "body" text NOT NULL, 
	        "date" date NOT NULL);
        COMMIT;