from django.contrib import admin

# Register your models here.
#superuser : gresiandrasmd, pass: admin123

from .import models

admin.site.register(models.sosmedModel)