from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Gorra(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="")

    def __str__(self):
        return self.nombre


class Remera(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="")

    def __str__(self):
        return self.nombre


class Pantalon(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="")

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos/")

    def __str__(self):
        return self.nombre
