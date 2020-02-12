from django.db import models

class School(models.Model):
	number = models.CharField('Номер', max_length=30)

	def __str__(self):
		return self.number

class Test(models.Model):
	title = models.CharField('Название', max_length=100)
	description = models.TextField('Описание')

	def __str__(self):
		return self.title

class Question(models.Model):
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	question = models.TextField('Вопрос')
	answer = models.CharField('Ответ', max_length=200)

	def __str__(self):
		return self.number