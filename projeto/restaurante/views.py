from django.shortcuts import render
from .models import Comida

# Create your views here.

def home(request):
    return render(request, 'index.html')

def cardapio(request):
    comidas = Comida.objects.all().order_by('nome_comida')
    return render(request, 'cardapio.html', {'comidas': comidas})

def reserva(request):
    return render(request, 'reserva.html')

def sobre(request):
    return render(request, 'sobre.html')
