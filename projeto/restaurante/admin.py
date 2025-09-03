from django.contrib import admin
from projeto.restaurante.models import TipoComida, Comida

# Register your models here.

class ComidaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ingredientes','tipo', 'valor')

class TipoComidaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'desc', 'composicao')

admin.site.register(Comida, ComidaModelAdmin)
admin.site.register(TipoComida, TipoComidaModelAdmin)
