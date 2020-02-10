import datetime
from login.models import User
def globalContext(request):
	email = request.session.get('email', None)
	password = request.session.get('password', None)
	user = isAuth(email, password)
	if user:
		name = user.name
		surname = user.surname
		age = user.age
		role = user.role
		auth=True
	else:
		auth=False
		user=surname=name=age=role=None
	context = {'year':datetime.datetime.now().year, 'name':name,'surname':surname, 'age':age, 'email':email, 'auth':auth, 'role':role}
	return context

def isAuth(email, password):
	try:
		user = User.objects.get(email=email, password=password)
		return user
	except:
		return False