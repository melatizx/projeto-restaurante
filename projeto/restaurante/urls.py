from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('reserva/', views.reserva, name='reserva'),
    path('sobre/', views.sobre, name='sobre'),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
]