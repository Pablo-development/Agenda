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
