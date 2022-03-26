from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    #IMAGEN

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

class Contrasena(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contrasena')
    plataforma = models.CharField(max_length=100)
    passw = models.CharField(max_length=100)

    def __str__(self):
        return f'Plataforma:{self.plataforma} Contrasena: {self.passw}'



