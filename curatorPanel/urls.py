from django.urls import path
from . import views

urlpatterns = [
	path('', views.curator, name='curator')
]