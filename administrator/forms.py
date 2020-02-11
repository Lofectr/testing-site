from django import forms
from .choice import ACTION_ADMIN_CHOICE

class SelectAction(forms.Form):
	select = forms.ChoiceField(choices=ACTION_ADMIN_CHOICE)

class AddCurator(forms.Form):
	name = forms.CharField(max_length=30)
	surname = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=100)