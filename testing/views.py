from django.shortcuts import render,redirect
from index.global_context import *
from login.models import *
from administrator.models import *

def testing(request):
	if 'ref' in request.GET:
		user = isReg(request.session.get('email',None), request.session.get('password', None)) #пользователь
		context = {}
		error = {}
		isError = False
		if user:
			isError = True
			error['isAuth'] = 'Извините, но персонал не может тестироваться'
		else:
			ref = request.GET['ref']
			classSchool = SchoolClass.objects.get(ref=ref)
			teacher = Teacher.objects.get(classSchool=classSchool)
			#Надо взять тест из учителя с проверкой на открытность, вывести вопросы, получить ответы, и в каждый выведеный вопрос добавить ответы, если он есть то просто увеличиваем Answer.count
		context['titlePage'] = 'Тестирование'
		context['error'] = error
		return render(request, 'testing.html', context)
	else:
		return redirect('/')