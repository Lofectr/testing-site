from django.shortcuts import render,redirect
from administrator.choice import REF_GENERATE_SIMBOL
from administrator.models import *
from random import choice
from login.models import Teacher
from index.global_context import *

def createRefForTesting(request):
	context = {}
	error = {}
	user = isReg(request.session.get('email',None), request.session.get('password', None)) #пользователь
	if user and isinstance(user, Teacher):

		context['listTest'] = {}
		for test in Test.objects.filter(isOpen=True):
			context['listTest'][test.id] = test.title

		if user.classSchool.ref:
			ref = user.classSchool.ref
			context['ref'] = ref
		if 'generateRefButton' in request.POST:
			isError = False
			if request.POST['listTest'] == 'default':
				isError = True
				error['default'] = 'Выберите тест для создания ссылки!'
			if not isError:
				while True:
					ref = ''
					for i in range(30):
						ref += choice(REF_GENERATE_SIMBOL)
					try:
						Teacher.objects.get(ref=ref)
					except:
						user.classSchool.ref = ref
						user.classSchool.save()
						context['ref'] = ref
						break
				testId = request.POST['listTest']
				test = Test.objects.get(id=testId)
				user.test = test
				user.save()
		context['titlePage'] = 'Создание ссылки'
		context['error'] = error
		return render(request, 'createRefForTesting.html', context)
	else:
		return redirect('/')