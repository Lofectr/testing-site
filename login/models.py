from django.db import models

class User(models.Model):
    email = models.EmailField('Почта',max_length=100)
    password = models.CharField('Пароль',max_length=10)
    name = models.CharField('Имя',max_length=30)
    surname = models.CharField('Фамилия',max_length=50)
    age = models.CharField('Возраст',max_length=3)
    role = models.CharField('Роль', max_length=30)

    def __str__(self):
        return self.email