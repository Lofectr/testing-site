from django.db import models
from administrator.models import *

class Admin(models.Model):
    email = models.EmailField('Почта',max_length=100)
    password = models.CharField('Пароль',max_length=15)
    name = models.CharField('Имя',max_length=30)
    surname = models.CharField('Фамилия',max_length=50)

    def __str__(self):
        return self.email

class Curator(models.Model):
    email = models.EmailField('Почта',max_length=100)
    password = models.CharField('Пароль',max_length=15)
    name = models.CharField('Имя',max_length=30)
    surname = models.CharField('Фамилия',max_length=50)

    def __str__(self):
        return self.email

class Teacher(models.Model):
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE)
    email = models.EmailField('Почта',max_length=100)
    password = models.CharField('Пароль',max_length=15)
    name = models.CharField('Имя',max_length=30)
    surname = models.CharField('Фамилия',max_length=50)
    classSchool = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.email