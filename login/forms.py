from django import forms
from .models import User

class Auth(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.PasswordInput()