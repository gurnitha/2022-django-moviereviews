# accounts/forms.py

# Django modules
from django.contrib.auth.forms import UserCreationForm


'''
created a new form UserCreateForm
which extends from UserCreationForm.
'''
# Form: UserCreateForm
class UserCreateForm(UserCreationForm):

	'''
	In the form’s constructor, def __init__(self,
	*args, **kwargs):, we call the super method.

	'''
	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		
		'''
		We set the help_text of the form’s fields to
		‘None’ to remove them, and we set for each
		form field a class attribute to use a Bootstrap
		class.
		'''
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
			self.fields[fieldname].widget.attrs.update({'class': 'form-control'})