from django.shortcuts import render, redirect
from .forms import UserForm, RegisterForm
from .models import Projects
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    projects = Projects.objects.filter(user=request.user).prefetch_related('tareas')

    return render(request, 'base.html', {
        'projects': projects
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pagina_inicio')
    else:
        form = AuthenticationForm()

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