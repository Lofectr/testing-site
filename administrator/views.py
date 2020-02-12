from django.shortcuts import render,redirect
from index.global_context import *
from .choice import *
import login
from .models import *
from random import choice

#админ панель
def administrator(request):
	user = isReg(request.session.get('email',None), request.session.get('password', None)) #пользователь
	current = "0"

	if user and isinstance(user, login.models.Admin):
		context = {}

		error = {}
		warning = {}

		if request.POST:
			#форма навигации
			if 'button_choose' in request.POST:

				current = request.POST.get('select')
				if current == '2':
					context['listCuratorsForDelete'] = {}
					for cur in login.models.Curator.objects.all():
						context['listCuratorsForDelete'][cur.id] = cur.surname+" "+cur.name+" | "+cur.email
				if current == '4':
					context['listSchoolForDelete'] = {}
					for school in School.objects.all():
						context['listSchoolForDelete'][school.id] = school.number
				if current == '6':
					context['listTestForUpdate'] = {}
					for test in Test.objects.all():
						context['listTestForUpdate'][test.id] = test.title
				if current == '7':
					context['listTestForDel'] = {}
					for test in Test.objects.all():
						context['listTestForDel'][test.id] = test.title
			#Добавить куратора
			elif 'addCuratorButton' in request.POST:
				current = '1'
				isError = False

				name = request.POST['name']
				surname = request.POST['surname']
				email = request.POST['email']
				password = ''
				for i in range(15):
					password += choice(PASSWORD_GENERATE_SIMBOL)

				#Валидность
				if isHaveEmailDB(email):
					isError = True
					error['email'] = 'Данный email уже занят :('
				if len(name) <= 1:
					isError = True
					error['name'] = 'Имя слишком короткое'
				if len(surname) <= 1:
					error['surname'] = 'Фамилия слишком короткая'
				if not isThisMail(email):
					error['email'] = 'Не корректный email'

				if not isError:
					newCurator = login.models.Curator(name=name, surname=surname, email=email,password=password)
					newCurator.save()


			#Удалить куратора
			elif 'delCuratorButton' in request.POST:
				current = '2'
				#удаление
				currentCurator = request.POST['listCuartorsDel']
				if currentCurator == "all":
					login.models.Curator.objects.all().delete()
				elif currentCurator == "default":
					error['listCurator'] = 'Выберите куратора'
				else:
					try:
						login.models.Curator.objects.get(id=currentCurator).delete()
					except:
						warning['all'] = 'Не надо подтверждать повторную отправку!'

				#заново показываем список
				context['listCuratorsForDelete'] = {}
				for cur in login.models.Curator.objects.all():
					context['listCuratorsForDelete'][cur.id] = cur.surname+" "+cur.name+" | "+cur.email


			#Добавить школу
			elif 'addSchoolButton' in request.POST:
				current = '3'
				number = request.POST['number']
				isError = False

				#Проверка на существование этой школы в базе данных
				try:
					school = School.objects.get(number=number)
					isError = True
					error['number'] = 'Данная школа уже существует'
				except:
					if len(number) < 2:
						isError = True
						error['number'] = 'Номер школы слишком короткий!'

					if not isError:
						newSchool = School(number=number)
						newSchool.save()

			elif 'delSchoolButton' in request.POST:
				current = '4'

				currentSchool = request.POST['listSchoolDel']
				if currentSchool == "default":
					error['listSchool'] = 'Выберите школу'
				else:
					try:
						School.objects.get(id=currentSchool).delete()
					except:
						warning['all'] = 'Не надо подтверждать повторную отправку!'

				#заново показываем список
				context['listSchoolForDelete'] = {}
				for school in School.objects.all():
					context['listSchoolForDelete'][school.id] = school.number


			#Добавление тестов
			elif 'addTestButton' in request.POST:
				isError = False
				current = '5'
				title = request.POST['title']
				description = request.POST['description']
				type_test = request.POST['selectClassTest']

				if len(title) < 3:
					isError = True
					error['title'] = 'Название слишком короткое!'
				if type_test == 'default':
					isError = True
					error['type_test'] = 'Выберите тип теста!'

				if not isError:
					test = Test(title=title, description=description)
					test.save()
					current = '6' #добавление/изменение вопросов
					context['listTestForUpdate'] = {}
					for test_ in Test.objects.all():
						context['listTestForUpdate'][test_.id] = test_.title
					context['currentTest'] = test.id
					context['isSelectedTest'] = True

			elif 'addUpdateTestButton' in request.POST:
				current = '6'
				isError = False

				currentTest = request.POST['listTestUpdate']
				context['currentTest'] = currentTest

				if currentTest == "default":
					isError = True
					error['listTest'] = 'Выберите тест!'
				else:
					try:
						test = Test.objects.get(id=currentTest)
					except:
						return redirect('/administrator/')
				#заново показываем список
				context['listTestForUpdate'] = {}
				for test_ in Test.objects.all():
					context['listTestForUpdate'][test_.id] = test_.title

				#можем добавлять вопросы
				if not isError:
					context['isSelectedTest'] = True
					context['listQuestion'] = test.question_set.all()

			elif 'addQuestionButton' in request.POST:
				current = '6'
				context['listTestForUpdate'] = {}
				for test in Test.objects.all():
					context['listTestForUpdate'][test.id] = test.title

				idTest = request.POST['currentTest']
				context['currentTest'] = idTest
				test = Test.objects.get(id=idTest)
				test.question_set.create(question='', answer='')
				context['listQuestion'] = test.question_set.all()
				context['isSelectedTest'] = True

			elif 'updateQuestionButton' in request.POST:
				current = '6'
				context['listTestForUpdate'] = {}
				for test in Test.objects.all():
					context['listTestForUpdate'][test.id] = test.title
				idTest = request.POST['currentTest']
				context['currentTest'] = idTest
				question = request.POST['question']
				answer = request.POST['answer']
				test = Test.objects.get(id=idTest)
				quest = test.question_set.get(id=request.POST['currentQuestion'])
				quest.question = question
				quest.answer = answer
				quest.save()

				context['listQuestion'] = test.question_set.all()
				context['isSelectedTest'] = True

			elif 'delQuestionButton' in request.POST:
				current = '6'
				context['listTestForUpdate'] = {}
				for test in Test.objects.all():
					context['listTestForUpdate'][test.id] = test.title
				idTest = request.POST['currentTest']
				context['currentTest'] = idTest
				test = Test.objects.get(id=idTest)
				test.question_set.get(id=request.POST['currentQuestion']).delete()

				context['listQuestion'] = test.question_set.all()
				context['isSelectedTest'] = True

			#удалить тест
			elif 'delTestButton' in request.POST:
				current = '7'
				currentTest = request.POST['listTestDel']
				if currentTest == "default":
					error['delTest'] = 'Выберите тест'
				else:
					try:
						Test.objects.get(id=currentTest).delete()
					except:
						warning['all'] = 'Не надо подтверждать повторную отправку!'

				#заново показываем список
				context['listTestForDel'] = {}
				for test in Test.objects.all():
					context['listTestForDel'][test.id] = test.title

			elif 'OpenTestButton' in request.POST:
				current = '8'

			elif '' in request.POST:
				current = '9'


		context['current'] = current
		context['error'] = error
		context['warning'] = warning
		return render(request, 'administrator.html', context)
	else:
		return redirect('/')

