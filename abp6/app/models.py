from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Projects(models.Model):
    name = models.CharField("Nombre",max_length=200)
    description = models.TextField("Descripción",blank=True)
    date_created = models.DateTimeField("Fecha de creación",auto_now_add=True)
    date_start = models.DateField("Fecha de inicio",null=True, blank=True)
    date_end = models.DateField("Fecha de finalización",null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
    
class Task(models.Model):
    STATUS = [
        ('P', 'Pendiente'),
        ('E', 'En progreso'),
        ('C', 'Completada'),
    ]

    title = models.CharField("Título",max_length=200)
    description = models.TextField("Descripción",blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='tareas', verbose_name="Proyecto")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Asignaso a")
    status = models.CharField("Estado",max_length=20, choices=STATUS, default='pendiente')
    date_create = models.DateTimeField("Fecha de creación",auto_now_add=True)
    expiration_date = models.DateField("Fecha de expiración",null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
