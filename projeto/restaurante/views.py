from django.shortcuts import render
from .models import TipoComida, Comida

# Create your views here.

def home(request):
    return render(request, 'index.html')

def cardapio(request):
    comidas = Comida.objects.all().order_by('tipo__nome','nome')
    tipocomidas = TipoComida.objects.all().order_by('nome')
    
    return render(request, 'cardapio.html', {
        'comidas': comidas, 'tipocomidas': tipocomidas
        })

def reserva(request):
    return render(request, 'reserva.html')

def sobre(request):
    return render(request, 'sobre.html')
