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
			try:
				classSchool = SchoolClass.objects.get(ref=ref)
				teacher = Teacher.objects.get(classSchool=classSchool)

				test = teacher.test
				context['titleTest'] = test.title
				context['questions'] = test.question_set.all()

				questionBan = request.session.get('questionBan', [])

				if request.POST:
					if 'answerButton' in request.POST:
						answerStr = request.POST['answer']
						question = Question.objects.get(id=request.POST['idQuestion'])
						questionBan.append(int(request.POST['idQuestion']))
						try:
							answer = classSchool.answer_set.get(question=question, answer=answerStr)
							answer.count = str(int(answer.count)+1)
							answer.save()
						except:
							classSchool.answer_set.create(count='1', question=question, answer=answerStr)
				context['questionBan'] = questionBan
				request.session['questionBan'] = questionBan
				if test.question_set.count() <= len(questionBan):
					del request.session['questionBan']
					context['isSuccess'] = True
			except:
				isError = True
				error['ref'] = 'Данный тест не найден :('

		context['titlePage'] = 'Тестирование'
		context['error'] = error
		context['isTesting'] = True
		return render(request, 'testing.html', context)
	else:
		return redirect('/')