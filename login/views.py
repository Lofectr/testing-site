from django.shortcuts import render
from django.shortcuts import redirect
from .forms import Auth
from .models import User
from django.contrib.auth import authenticate, login

def auth(request):
    if request.POST:
        formAuth = Auth(request.POST)
        if formAuth.is_valid():
            if User.objects.filter(email=request.POST['email'], password=request.POST['password']):
                request.session['email'] = request.POST['email']
                request.session['password'] = request.POST['password']
                return redirect('/')
            return redirect('/auth/')
    else:
        form = Auth()
    return render(request, 'auth.html', {'form':form})