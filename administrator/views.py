from django.shortcuts import render,redirect
from index.global_context import isAuth

def administrator(request):
	user = isAuth(request.session.get('email',None), request.session.get('password', None))
	if user and user.role=="Admin":
		print(request.POST.get('current') or "0")
		return render(request, 'administrator.html', {'current':request.POST.get('current') or "0"})
	else:
		return redirect('/')