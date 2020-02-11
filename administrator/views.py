from django.shortcuts import render,redirect
from index.global_context import *
from .forms import *
from .choice import *
import login
from random import choice

def administrator(request):
	user = isReg(request.session.get('email',None), request.session.get('password', None))
	current = "0"
	if user and isinstance(user, login.models.Admin):
		if request.POST:
			#форма навигации
			if 'button_choose' in request.POST: #доп. проверка на какую кнопку нажали(лишним не будет)
				form = SelectAction(request.POST)
				current = request.POST.get('select')
		else:
			form = SelectAction()
		return render(request, 'administrator.html', {'form':form, 'current':current})
	else:
		return redirect('/')

def add_curator(request):
	user = isReg(request.session.get('email',None), request.session.get('password', None))
	if user and isinstance(user, login.models.Admin):
		if request.POST:
			if 'addCuratorButton' in request.POST:
				name = request.POST['name']
				surname = request.POST['surname']
				email = request.POST['email']
				password = ''
				for i in range(15):
					password += choice(PASSWORD_GENERATE_SIMBOL)
				print(password)
				newCurator = login.models.Curator(name=name, surname=surname, email=email,password=password)
				newCurator.save()
				return redirect('/administrator/')
		else:
			#если админ сам зашел сюда, то мы его выкидываем
			return redirect('/')
	else:
		#если это не админ, а пользователь
		return redirect('/')