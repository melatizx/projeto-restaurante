from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario



class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome','email','cpf']
    search_fields = ('email','cpf')

admin.site.register(Usuario, UsuarioAdmin)
