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
	def __str__(self):
		return self.question
class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.CharField('Ответ', max_length=150)

	def __str__(self):
		return self.answer
class SchoolClass(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	number = models.CharField('Номер класса', max_length=2)
	char = models.CharField('Буква класса', max_length=1)
	length = models.CharField('Кол-во учеников', max_length=2)
	ref = models.CharField('Ссылка на тестирование', max_length=50)

	def __str__(self):
		return self.number + self.char