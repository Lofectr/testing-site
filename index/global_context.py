import datetime
import login
def globalContext(request):
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