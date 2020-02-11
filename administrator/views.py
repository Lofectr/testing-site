from django.shortcuts import render,redirect
from index.global_context import *
from .choice import *
import login
from .models import *
from random import choice

#админ панель
def administrator(request):
	user = isReg(request.session.get('email',None), request.session.get('password', None))
	current = "0"
	if user and isinstance(user, login.models.Admin):
		if request.POST:
			#форма навигации
			if 'button_choose' in request.POST:
				current = request.POST.get('select')
			elif 'addCuratorButton' in request.POST:
				name = request.POST['name']
				surname = request.POST['surname']
				email = request.POST['email']
				password = ''
				for i in range(15):
					password += choice(PASSWORD_GENERATE_SIMBOL)
				newCurator = login.models.Curator(name=name, surname=surname, email=email,password=password)
				newCurator.save()
			elif 'addSchoolButton' in request.POST:
				number = request.POST['number']
				newSchool = School(number=number)
				newSchool.save()

		return render(request, 'administrator.html', {'current':current})
	else:
		return redirect('/')