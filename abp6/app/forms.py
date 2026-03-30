from django import forms
from .models import Projects, Task, User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.Form):
    username = forms.CharField(max_length=20, error_messages={'max_length':'nombre muy largo'},
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-4',
            'placeholder': 'Nombre de usuario',
            'autocomplete': 'off'
        }))
    password = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'type': 'password',
            'autocomplete': 'off'
        }))

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico'
        })
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })
            
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nombre de usuario'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repetir contraseña'
        })