from django.shortcuts import render
from .models import Pessoa

# Create your views here.

def home(request):
    return render(request, 'index.html')

def cardapio(request):
    return render(request, 'cardapio.html')

def reserva(request):
    return render(request, 'reserva.html')

def sobre(request):
    return render(request, 'sobre.html')

def lista_pessoas(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'pessoas.html', {'pessoas': pessoas})