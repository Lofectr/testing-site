from django.urls import path
from . import views

urlpatterns = [
	path('', views.administrator, name='administrator'),
	path('add_curator/', views.add_curator, name="add_curator")
]