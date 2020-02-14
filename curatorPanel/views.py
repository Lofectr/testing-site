from django.shortcuts import render

from django.shortcuts import render,redirect
from index.global_context import *
import login
from random import choice

#куратор панель
def curator(request):
	user = isReg(request.session.get('email',None), request.session.get('password', None)) #пользователь
	current = "0"

	if user and isinstance(user, login.models.Curator):
		context = {}

		error = {}
		warning = {}

		if request.POST:
			#форма навигации
			if 'button_choose' in request.POST:
				current = request.POST.get('select')
				if current == '2':
					context['listTeacherForDelete'] = {}
					for teacher in user.teacher_set.all():
						context['listTeacherForDelete'][teacher.id] = teacher.surname+" "+teacher.name+" | "+teacher.email

				if current == '1':
					if 'searchTeacher' in request.POST:
						context['Teachers'] = user.teacher_set.filter(email__startwith=request.POST['searchTeacher'])
					else:
						context['Teachers'] = user.teacher_set.filter()
			
			elif 'delTeacherButton' in request.POST:
				current = '2'
				#удаление
				currentTeacher = request.POST['listTeacherDel']
				if currentTeacher == "all":
					user.teacher_set.all().delete()
				elif currentTeacher == "default":
					error['listTeacher'] = 'Выберите учителя!'
				else:
					try:
						user.teacher_set.get(id=currentTeacher).delete()
					except:
						warning['all'] = 'Не надо подтверждать повторную отправку!'

				#заново показываем список
				context['listTeacherForDelete'] = {}
				for teacher in user.teacher_set.all():
					context['listTeacherForDelete'][teacher.id] = teacher.surname+" "+teacher.name+" | "+teacher.email

			elif 'searchTeacher' in request.POST:
				current = '1'
				context['Teachers'] = user.teacher_set.filter(email__startswith=request.POST['searchTeacher'])
		context['current'] = current
		context['error'] = error
		context['warning'] = warning
		context['titlePage'] = 'Куратор панель'
		return render(request, 'curatorPanel.html', context)
	else:
		return redirect('/')