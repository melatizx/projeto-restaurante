from django.contrib import admin
from projeto.restaurante.models import Pessoa

# Register your models here.

class PessoaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_nascimento')

admin.site.register(Pessoa, PessoaModelAdmin)