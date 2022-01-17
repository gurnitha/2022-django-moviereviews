# accounts/views.py

# Django modules
from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError

# Locals
from accounts.forms import UserCreateForm

# Create your views here.

def signupaccount(request):

	'''
	We first check if the
	request received is a GET or POST request. If
	it is a GET request, it means that it’s a user
	navigating to the sign up form via the url
	localhost:8000/accounts/signupaccount, in
	which case we simply send them to
	signupaccount.html with the form.

	But if it’s a POST request, it means that it’s a
	form submission to create a new user. And
	we move to the else block to create a new
	user.
	'''
	if request.method == 'GET':
		return render(request, 'accounts/signupaccount.html', {'form':UserCreateForm})

	else:
		'''
		ensure that the password
		entered into password1 and password2 are
		the same before going on to create the user.

		So we first ensure that the
		password and confirm password values are
		the same before proceeding.
		'''
		if request.POST['password1'] == request.POST['password2']:
			'''
			We then retrieve the data entered into the
			username field (request.POST['username'])
			and password field
			(password=request.POST['password1']).

			We pass in the data into User.objects.create_user
			which helps us create the user object. 

			The User model is provided
			by Django’s Auth app (from
			django.contrib.auth.models import User)
			which has the User model in the database
			setup for us.

			if the user signs up with a username
			that already exists in the database. To catch
			such an error that is thrown by the database,
			we have to use try and except
			'''
			try:
				user = User.objects.create_user(
						request.POST['username'], 
						password=request.POST['password1'])

				'''
				user.save() actually inserts the new user into
				the database. The newly added user will show
				up in Users in Admin.
				'''
				user.save()

				'''
				After creating the user, we then login with the
				new user. 

				That is, after someone signs up, we
				automatically log them in and redirect them
				to the home page.
				'''
				login(request, user)
				return redirect('movie:home')

				'''
				if the user signs up with a username
				that already exists in the database. To catch
				such an error that is thrown by the database,
				we have to use try and except
				'''
			except IntegrityError:
				return render(request, 'accounts/signupaccount.html', {'form':UserCreateForm, 'error':'Username already taken. Choose new username.'})
		
			'''
			If the passwords don’t match, we render the
			user back to signupaccount.html and also
			pass in an error message ‘Passwords do not
			match’.
			'''
		else:
			return render(request, 'accounts/signupaccount.html', {'form':UserCreateForm, 'error':'Passwords do not match'})


	return render(request, 'accounts/signupaccount.html', {'form':UserCreateForm})


def logoutaccount(request):
	logout(request)
	return redirect('movie:home')


def loginaccount(request):

	'''
	loginaccount will be similar to
	signupaccount. 

	We first check if the
	request received is a GET or POST request. If
	it is a GET request, it means that it’s a user
	navigating to the sign up form via the url
	localhost:8000/accounts/loginaccount, in
	which case we simply send them to
	loginaccount.html with the form.

	But if it’s a POST request, it means that it’s a
	form submission to create a new user. And
	we move to the else block to create a new
	user.
	'''

	if request.method == 'GET':
		return render(request, 'accounts/loginaccount.html', {'form':AuthenticationForm})

		'''
		Much like the
		UserCreationForm for signup, Django
		provides the AuthenticationForm to quickly
		get a login form up and running.

		If the request type is not GET (user submits
		the login form and sends a POST request), we
		proceed to authenticate the user with the
		values he entered in the username and
		password fields.	
		'''
	else:
		user = authenticate(request,
				username=request.POST['username'],
				password=request.POST['password'])

		'''
		If the user returned from authenticate is
		None, i.e. we are unable to find an existing
		user with the supplied username/password,
		we return the user to loginaccount.html with
		the error ‘username and password do not
		match’ 
		'''
		if user is None:
			return render(request,'accounts/loginaccount.html', {'form': AuthenticationForm(), 'error': 'username and password do not match'})
		
			'''
			Else, it means the authentication is successful
			and we log in the user and redirect her to the
			home page.
			'''
		else:
			login(request,user)
			return redirect('movie:home')

