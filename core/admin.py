from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):    #classe para listar em tela os atributos abaixo no /admin
    list_display = ('Titulo', 'data_evento', 'data_criacao')

admin.site.register(Evento, EventoAdmin)