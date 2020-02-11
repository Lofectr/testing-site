from django.contrib import admin
from . import models
admin.site.register(models.Admin)
admin.site.register(models.Curator)
admin.site.register(models.Teacher)