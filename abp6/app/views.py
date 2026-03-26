from django.shortcuts import render, redirect
from .forms import UserForm, RegisterForm

from django.contrib.auth import login

# Create your views here.

def home(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            return render(request, 'resultado.html', {
                'nombre': name,
                'email': email,
                'contrasena': password
            })
    else:
        form = UserForm()

    return render(request, 'login.html', {'form': form})

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