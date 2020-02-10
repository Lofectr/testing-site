from django.shortcuts import render, redirect
from login.models import User
from .global_context import isAuth

def index(request):
	user = isAuth(request.session.get('email', None), request.session.get('password',None))
	if user:
		return render(request, 'index.html')
	else:
		return redirect('/auth/')