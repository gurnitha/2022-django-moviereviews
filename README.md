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


#### 14. Displaying objects in Admin

        modified:   README.md
        modified:   movie/models.py


#### 15. Extending Base Templates

        Works:

        1. Create base tamplate file
        2. Activate Django template
        3. Extends base template to all pages
        4. Add footer to base template

        modified:   README.md
        modified:   config/settings.py
        new file:   config/templates/base.html
        modified:   movie/templates/movie/about.html
        modified:   movie/templates/movie/home.html
        modified:   movie/templates/movie/signup.html
        modified:   news/templates/news/news.html


#### 16. Static Files

        Works: 

        1. Create static folder
        2. Add static files to it
        3. Create path for static files
        4. Load tatic files

        modified:   README.md
        modified:   config/settings.py
        new file:   config/static/images/movie.png
        modified:   config/templates/base.html
        modified:   movie/templates/movie/about.html
        modified:   movie/templates/movie/home.html
        modified:   movie/templates/movie/signup.html
        modified:   news/templates/news/news.html


#### 17. Movie Detail Page

        Works:

        1. Create movie detail page
        2. Create movie detail path
        3. Create view detail
        4. Add link in home page to go to page detail

        new file:   movie/templates/movie/detail.html
        modified:   movie/templates/movie/home.html
        modified:   movie/urls.py
        modified:   movie/views.py


#### 18 & 19. Creating A Signup Form and Creating A User


#### 18 & 19.1 Sign up a new user using the default UserCreationForm

        When the user submits the signup form, we
        will have to handle the request and create a
        user in admin. To do so, do these:

        Works:

        1. Create a new app called 'accounts'
        2. Create signupaccount page
        3. Create path
        4. Create signupaccount view with signup logic
        5. Test it out by sign up new user :)

        modified:   README.md
        new file:   accounts/__init__.py
        new file:   accounts/admin.py
        new file:   accounts/apps.py
        new file:   accounts/migrations/__init__.py
        new file:   accounts/models.py
        new file:   accounts/templates/accounts/signupaccount.html
        new file:   accounts/tests.py
        new file:   accounts/urls.py
        new file:   accounts/views.py
        modified:   config/settings.py
        modified:   config/templates/base.html
        modified:   config/urls.py


#### 18 & 19.2 Customizing UserCreationForm

        The UserCreationForm currently shows quite
        a lot of extra help text (included by default)
        which are cluttering our form. 

        We can actually customize the UserCreationForm
        which is a big topic on its own. Here, we will
        simply remove the default help text.

        To customize the form, we have to create a
        new class which extends UserCreationForm.

        Works:

        1. Create a new file forms.py
        2. Withing it, create UserCreateForm class with  logic
        3. Modify signupaccount view
        4. Test it out :)

        modified:   README.md
        new file:   accounts/forms.py
        modified:   accounts/views.py


#### 18 & 19.3 House keeping: Modified README.md file

        modified:   README.md


#### 20. Showing If A User Is Logged In

        Works:

        1. Add conditional to navbar

        modified:   README.md
        modified:   config/templates/base.html


#### 21. Logout

        Works:

        1. Create path for logout
        2. Create logout view
        3. Add link to navbar

        modified:   README.md
        modified:   accounts/urls.py
        modified:   accounts/views.py
        modified:   config/templates/base.html


#### 22. Log In

        Works:

        1. Create login page
        2. Create path for login
        3. Create loin view
        4. Add link to navbar
        5. Test it out :)

        modified:   README.md
        new file:   accounts/templates/accounts/loginaccount.html
        modified:   accounts/urls.py
        modified:   accounts/views.py
        modified:   config/templates/base.html


#### 23. Letting User To Post Movie Review

        We will now implement letting logged-in
        users post reviews for movies. 

        Works:

        1. Create Review model, add relationship with User and Movie models

        modified:   README.md
        modified:   movie/admin.py
        new file:   movie/migrations/0002_review.py
        modified:   movie/models.py


#### 24. Creating A Review

        We have seen how to create model objects
        from the admin e.g. creating a movie object.
        But how do we allow users to create their
        own objects e.g. let users post a review from
        the site? After all, not everyone should have
        access to the admin panel.

        Works:

        1. Create ReviewForm class
        2. Create createreview page
        3. Create createreview view
        4. Create path for review
        5. Add link with detail
        6. Test it out :)

        NOTE: Instance of the reviews save in db

        modified:   README.md
        new file:   movie/forms.py
        new file:   movie/templates/movie/createreview.html
        modified:   movie/templates/movie/detail.html
        modified:   movie/urls.py
        modified:   movie/views.py


#### 25. Listing Review

        Works:

        1. Modify the detail view
        2. Modify the detail page to render the reviews

        modified:   README.md
        modified:   movie/templates/movie/detail.html
        modified:   movie/views.py



#### 26. Updating A Review

        Works:

        1. Create updatereview page
        2. Create updatereview view
        3. Create path to update review
        4. Add link with detail page
        5. Test it out :)


        modified:   README.md
        modified:   movie/templates/movie/detail.html
        new file:   movie/templates/movie/updatereview.html
        modified:   movie/urls.py
        modified:   movie/views.py

