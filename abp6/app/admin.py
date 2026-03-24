from django.contrib import admin
from .models import Projects, Task


# Register your models here.

admin.site.register(Projects)
admin.site.register(Task)

admin.site.site_header = "Panel de Administración"
admin.site.site_title = "Administración TaskManager"