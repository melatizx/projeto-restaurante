from django.contrib import admin
from projeto.restaurante.models import Comida

# Register your models here.

class ComidaModelAdmin(admin.ModelAdmin):
    list_display = ('nome_comida', 'ingredientes', 'valor')

admin.site.register(Comida, ComidaModelAdmin)