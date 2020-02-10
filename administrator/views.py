from django.shortcuts import render,redirect
from index.global_context import isAuth
from .forms import SelectAction

def administrator(request):
	user = isAuth(request.session.get('email',None), request.session.get('password', None))
	current = "0"
	if user and user.role=="Admin":
		if request.POST:
			form = SelectAction(request.POST)
			current = request.POST.get('select')
		else:
			form = SelectAction()
		return render(request, 'administrator.html', {'form':form, 'current':current})
	else:
		return redirect('/')