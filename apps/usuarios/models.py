from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.


class Usuarios(AbstractUser):
    nombre = models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True, blank=True, default='1940-1-1')

    es_colaborador = models.BooleanField('Es_colaborador',default=False)
    
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios', default='usuarios/pordefecto.jpg')
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    def __str__(self):
        return self.nombre

    
