from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Headword)
admin.site.register(models.POS)
admin.site.register(models.Meaning)