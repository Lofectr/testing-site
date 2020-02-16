from django.shortcuts import render, redirect
from index.global_context import *
import login
from administrator.models import *
from random import choice
from administrator.choice import *
email = None
password = None
name = None
def regTeacher(request):
	context = {}
	error = {}
	context['listSchoolForReg'] = {}
	for school in School.objects.all():
		context['listSchoolForReg'][school.id] = school.number
	context['listCuratorForReg'] = {}
	for cur in login.models.Curator.objects.all():
		context['listCuratorForReg'][cur.id] = cur.surname+" "+cur.name+" | "+cur.email
	if request.POST:
		isError = False
		global email, password, name

		name = request.POST['name']
		surname = request.POST['surname']
		email = request.POST['email']
		curatorId = request.POST['listCurator']
		schoolId = request.POST['listSchool']
		numberClass = request.POST['class']
		charClass = request.POST['char']
		lengthClass = request.POST['length']
		password = ''
		for i in range(15):
			password += choice(PASSWORD_GENERATE_SIMBOL)

		if isHaveEmailDB(email):
			isError = True
			error['email'] = 'Данный email уже занят :('
		if len(name) < 2:
			isError = True
			error['name'] = 'Имя слишком короткое!'
		if len(surname) < 2:
			isError = True
			error['surname'] = 'Фамилия слишком короткая!'
		if schoolId == 'default':
			isError = True
			error['schoolList'] = 'Выберите школу!'
		if curatorId == 'default':
			isError = True
			error['curatorList'] = 'Выберите куратора!'

		if not isError:
			curator = login.models.Curator.objects.get(id=curatorId)
			school = School.objects.get(id=schoolId)
			try:
				schoolclass = SchoolClass.objects.get(number=numberClass, char=charClass, school=school)
				error['class'] = 'Этот класс уже существует, вы наверное не учитель, или какой-то плохой человек(не учитель) зарегистрировал этот класс :('
			except:
				classSchool = SchoolClass(number=numberClass, char=charClass, length=lengthClass, ref='', school=school)
				classSchool.save()
				newTeacher = curator.teacher_set.create(email=email, password=password, name=name, surname=surname, classSchool=classSchool) #test=test
				context['isReg'] = True
				context['password'] = password
				return redirect('success-reg/')
	context['error'] = error
	context['titlePage'] = 'Регистрация учителей'
	return render(request, 'regTeacher.html', context)

def successReg(request):
	return render(request, 'successReg.html', {'new_email':email, 'new_password': password, 'new_name': name,'titlePage':'Успешная регистрация!'})