from django.shortcuts import render

from core.models import Evento


# Create your views here.

def lista_eventos(request):
    evento = Evento.objects.all()#puxando todos os eventos do banco de dados
    #há a possibilidade de filtrar os eventos por meio de usuarios da seguinte forma:
    usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario) --> dessa forma, os eventos serão filtrados por usuario
    dados = {'eventos': evento}
    return render(request, "agenda.html", dados)