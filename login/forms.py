from django import forms

class Auth(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.PasswordInput()