from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Post)
admin.site.register(models.Catgory)
admin.site.register(models.Comment)