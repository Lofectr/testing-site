import datetime
import login
from administrator.models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def globalContext(request):
	closeTestOrNot()
	clearTeacherRefIfTestNone()
	email = request.session.get('email', None)
	password = request.session.get('password', None)
	user = isReg(email, password)
	if user:
		name = user.name
		surname = user.surname
		auth=True

		if isinstance(user, login.models.Admin):
			role="Admin"
		elif isinstance(user, login.models.Curator):
			role="Curator"
		elif isinstance(user, login.models.Teacher):
			role="Teacher"
	else:
		auth=False
		user=surname=name=role=None
	context = {'year':datetime.datetime.now().year, 'name':name,'surname':surname, 'email':email, 'auth':auth, 'role':role}
	return context

def isReg(email, password):
	try:
		user = login.models.Admin.objects.get(email=email, password=password)
		return user
	except:
		try:
			user = login.models.Curator.objects.get(email=email, password=password)
			return user
		except:
			try:
				user = login.models.Teacher.objects.get(email=email, password=password)
				return user
			except:
				return False

def isHaveEmailDB(email):
	try:
		user = login.models.Admin.objects.get(email=email)
		return True
	except:
		try:
			user = login.models.Curator.objects.get(email=email)
			return True
		except:
			try:
				user = login.models.Teacher.objects.get(email=email)
				return True
			except:
				return False #Значит почта свободна

def isThisMail(email):    
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def closeTestOrNot():
	dateNow = datetime.datetime.now()
	for test in Test.objects.filter(isOpen=True):
		dateEnd = datetime.datetime(year=test.end.year, month=test.end.month, day=test.end.day)
		if dateEnd <= dateNow:
			test.isOpen = False
			test.end = None
			test.save()

def clearTeacherRefIfTestNone():
	for teacher in login.models.Teacher.objects.all():
		if teacher.test == None:
			if teacher.classSchool.ref != '':
				teacher.classSchool.ref = ''
				teacher.classSchool.save()
		else:
			if teacher.test.isOpen == False:
				teacher.test = None
				teacher.save()
				if teacher.classSchool.ref != '':
					teacher.classSchool.ref = ''
					teacher.classSchool.save()