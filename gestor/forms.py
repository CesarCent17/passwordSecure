from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contrasena

class RegistroUsuario(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite tu contrasena', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {label:"" for label in fields}

class RegistroContrasena(forms.ModelForm):
    plataforma = forms.CharField(label='Plataforma')
    passw = forms.CharField(label='Contrasena', widget=forms.PasswordInput)

    class Meta:
        model = Contrasena
        fields = ['plataforma', 'passw']

