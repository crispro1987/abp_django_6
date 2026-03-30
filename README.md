# Django Web App
## Proyecto Módulo #6 | ABP

plataforma web que permite a los usuarios gestionar tareas y proyectos de forma eficiente.

## Video Demostrativo

[![Ver video](https://img.youtube.com/vi/Sgdi3-7ef4w/0.jpg)](https://youtu.be/Sgdi3-7ef4w)

## Tecnologías utilizadas

- Python 3.14
- asgiref  3.11.1
- Django   6.0.2
- pip      26.0.1
- sqlparse 0.5.5
- tzdata   2025.3
- Github

## Estructura del proyecto

```
abp6/
│
├── abp6/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.txt
├── app/
│   ├── migrations/
│   ├── templates/
│   │   ├── 404.html
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── project.html
│   │   ├── register.html
│   │   └── task.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── test.py
│   ├── urls.py
|   └── views.py
├── static/
|   ├── css/
│   │   └── style.css
│   └── img/
│       └── logo.png
├── db.sqlite3
├── manage.py
└── README.md

```

## Gestión de usuarios

Implementación un sistema de registro y autentificación de usuarios.

```
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('pagina_inicio')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')

    else:
        form = UserForm()

    return render(request, 'login.html', {'form': form})
```

Configurar redirecciones post-login y logout

```
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'pagina_inicio'
LOGOUT_REDIRECT_URL = 'pagina_inicio'
```

## Gestión de tareas y proyectos

Creación de modelos

```
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
```

Implementar relaciones entre usuarios y proyectos

```
user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
```

## Interfaz de usuario con Templates de Django

Herencia de plantillas para mantener estructura modular

```
{% extends 'base.html' %}

{% block title %}Proyecto{% endblock %}

{% block content %}
```

Implementar formularios con validaciones

```
<form method="POST">
    {% csrf_token %}

    {% for field in form %}
                    
        <div class="mb-3">
            {{ field }}
        </div>
        {% if field.errors %}
        <div class="text-danger small">
            {{ field.errors }}
        </div>
        {% endif %}
    {% endfor %}
```

## Sitio administrativo de Django

Registrar modelos

```
from .models import Projects, Task

admin.site.register(Projects)
admin.site.register(Task)
```

## Seguridad y validaciones

Implementar protección CSRF

```
 <form method="POST">
    {% csrf_token %}

    {% for field in form %}
```
