from django.urls import path
from . import views

urlpatterns = [
	path('', views.regTeacher, name='regTeacher'),
	path('success-reg/', views.successReg, name='successReg')
]