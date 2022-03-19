import datetime
from email.policy import default
from unittest.util import _MAX_LENGTH
from django import forms
from landscape.models import Like, Review

ACTIVITIES = (
	("boating", "Boating"), 
	("none", "None"), 
	("camping", "Camping"), 
	("fishing", "Fishing"), 
	("hiking", "Hiking"), 
	("swimming", "Swimming")
)

FACILITIES = (
	("none", "None"), 
	("kids-area", "Kid's area"), 
	("parking", "Parking"), 
	("pet-friendly", "Pet friendly"), 
	("toilets", "Toilets"), 
	("wheelchair", "Wheelchair")
)

class ReviewForm(forms.ModelForm):
	title = forms.CharField(max_length=Review.TITLE_MAX_LENGTH, help_text="Title")
	description = forms.CharField(help_text="Description", required=False)
	rating = forms.IntegerField(help_text="Rating", initial=0)
	activities =  forms.MultipleChoiceField(choices = ACTIVITIES, initial=['none'], required=False)
	facilities =  forms.MultipleChoiceField(choices = FACILITIES, initial=['none'], required=False)
    
	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Review
		fields = ('title','description', 'rating', 'visit_date', 'facilities', 'activities')

class LikeForm(forms.ModelForm):    
	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Like
		fields = ('date',)