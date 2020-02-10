from django import forms
from .choice import ACTION_ADMIN_CHOICE

class SelectAction(forms.Form):
	select = forms.ChoiceField(choices=ACTION_ADMIN_CHOICE)