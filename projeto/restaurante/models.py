from django.db import models

# Create your models here.

COMPOSICAO_CHOICE = [
        ('e', 'Entradas'),
        ('p','Principais'),
        ('s','Sobremesas'),
        ('b', 'Bebidas'),
        ('o', 'Outros'),
]
class TipoComida(models.Model):
    nome = models.CharField(max_length=100)
    desc = models.TextField()

    composicao = models.CharField(
        choices=COMPOSICAO_CHOICE,
        default='o',
    )
    
    def __str__(self):
        return self.nome    

class Comida(models.Model):    
    nome = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=500)
    valor = models.PositiveIntegerField()
    tipo = models.ForeignKey(TipoComida, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome