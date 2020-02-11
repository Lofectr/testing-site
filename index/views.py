from django.shortcuts import render, redirect
from .global_context import *
import login

def index(request):
	user = isReg(request.session.get('email', None), request.session.get('password',None))
	if user:
		return render(request, 'index.html')
	else:
		return redirect('/auth/')