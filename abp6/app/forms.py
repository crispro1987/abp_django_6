from django import forms
from .models import Projects, Task, User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.Form):
    name = forms.CharField(label='Nombre',max_length=20, error_messages={'max_length':'nombre muy largo'})
    email = forms.EmailField(label='Correo',error_messages={'invalid':'Correo No valido'})
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')