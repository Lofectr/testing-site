from django.db import models

class School(models.Model):
	number = models.CharField('Номер', max_length=30)

	def __str__(self):
		return self.number