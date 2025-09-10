from django.urls import path
from . import views


urlpatterns= [
    path('', views.home, name='home'),
    path('enter/', views.enter, name='enter'),
    path('perfil/', views.perfil, name='perfil'),
]