from django.db import models

# Create your models here.

class Comida(models.Model):
    nome_comida = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=500)
    valor = models.PositiveIntegerField()