from django.shortcuts import render,redirect
from administrator.choice import REF_GENERATE_SIMBOL
from random import choice
from login.models import Teacher
from index.global_context import *

def createRefForTesting(request):
	context = {}
	user = isReg(request.session.get('email',None), request.session.get('password', None)) #пользователь
	if user and isinstance(user, Teacher):
		if user.classSchool.ref:
			ref = user.classSchool.ref
			context['ref'] = ref
		if 'generateRefButton' in request.POST:
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
		context['titlePage'] = 'Создание ссылки'
		return render(request, 'createRefForTesting.html', context)
	else:
		return redirect('/')