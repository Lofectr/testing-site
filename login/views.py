from django.shortcuts import render, redirect
from .models import *
from index.global_context import *

def auth(request):
    if request.POST:
        if isReg(request.POST['email'],request.POST['password']):
            request.session['email'] = request.POST['email']
            request.session['password'] = request.POST['password']
            return redirect('/')
        return redirect('/auth/')
    return render(request, 'auth.html', {'titlePage':'Авторизация'})

def exit(request):
	try:
		del request.session['email']
		del request.session['password']
		return redirect('/') 
	except:
		return redirect('/')