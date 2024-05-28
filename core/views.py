from django.contrib import messages

from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@login_required(login_url='/login/') #caso nao possua autenticação, sera direcionado para 'login'
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) #filtragem por usuario
    dados = {'eventos': evento} #dict
    return render(request, "agenda.html", dados)

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou senha incorretos')
    return redirect('/')
@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST['titulo']
        data_evento = request.POST['data_evento']
        descricao = request.POST['descricao']
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.save()
        else:
            local = request.POST['local']
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario,
                                  local=local)
    return redirect('/')
@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')