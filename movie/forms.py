# movie/forms.py

# Django modules
from django.forms import ModelForm, Textarea

# Locals
from movie.models import Review

# Form: ReviewForm
# We need to inherit from ModelForm.
class ReviewForm(ModelForm):

	'''
	Similar as what we did with the
	UserCreationForm, we set some Bootstrap
	classes for our form fields.
	'''
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['text'].widget.attrs.update( {'class': 'form-control'})
		self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})

		'''
		We then specify which model the form is for
		and the fields we want in the form. In our
		case, our review form will need just the text
		and watchAgain fields. If you recall, in our
		Review model:
		class Review(models.Model):
			text = models.CharField(max_length=100)
			date = models.DateTimeField(auto_now_add=True)
			user =
			models.ForeignKey(User,on_delete=models.CASCADE)
			movie =
			models.ForeignKey(Movie,on_delete=models.CASCADE)
			watchAgain = models.BooleanField()
		date is auto-populated, user and movie are
		already provided. Thus, we need only user to
		input the text and watchAgain fields in the
		form.
		'''
	class Meta:
		model = Review
		fields = ['text','watchAgain']
		'''
		We have a labels object where we can create
		custom labels for each of our fields. For e.g.,
		we want to display ‘ Watch Again ’ instead
		of watchAgain (our users are not
		programmers!).
		'''
		labels = {'watchAgain': ('Watch Again')}

		'''
		By default, a CharField is displayed as an
		input text. We override this default field (with
		the use of widgets) to have a Textarea for our
		text field.

		'''
		widgets = {'text': Textarea(attrs={'rows': 4}),}
