import datetime
from django import forms
from landscape.models import Review

class ReviewForm(forms.ModelForm):
	title = forms.CharField(max_length=Review.TITLE_MAX_LENGTH, help_text="Title")
	description = forms.CharField(help_text="Description", required=False)
	rating = forms.IntegerField(help_text="Rating", initial=0)
	#image = forms.ImageField()
    
	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Review
		fields = ('title','description', 'rating', )