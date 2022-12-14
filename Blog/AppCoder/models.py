from django.db import models

# Create your models here.
class Videojuegos(models.Model):
    nombre=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    ano_lanzamiento=models.IntegerField()

class Plataformas(models.Model):
    nombre=models.CharField(max_length=40)
    precio=models.IntegerField()
    ano_lanzamiento=models.IntegerField()

class Hardware(models.Model):
    nombre=models.CharField(max_length=40)
    distribuidor=models.CharField(max_length=40)
    precio=models.IntegerField()