from django.db import models

# Create your models here.

class TipoComida(models.Model):
    nome = models.CharField(max_length=100)
    desc = models.TextField()

class Comida(models.Model):    
    nome = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=500)
    valor = models.PositiveIntegerField()
    tipo = models.ForeignKey(TipoComida, blank=True, null=True, on_delete=models.SET_NULL)