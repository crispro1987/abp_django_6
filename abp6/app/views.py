from django.shortcuts import render, redirect
from .forms import UserForm, RegisterForm
from .models import Projects
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        projects = Projects.objects.filter(user=request.user).prefetch_related('tareas')
    else:
        projects = Projects.objects.none()

    return render(request, 'base.html', {
        'projects': projects
    })


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

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pagina_inicio')
    else:
        form = RegisterForm()

    return render(request, "register.html",{"form":form})

def error_404(request):
    return render(request, '404.html', status=404)

@login_required
def project_view(request):
    return render(request, 'project.html')

@login_required
def task_view(request):
    return render(request, 'task.html')