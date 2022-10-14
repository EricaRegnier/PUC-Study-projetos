from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegistroForm, RegistroAvaliacaoForm


def index(request):
    return render(request, 'index.html')


def registroUsuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password1')
            usuario = authenticate(username=username, password=senha)
            login(request, usuario)
            return redirect('menu')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form} )


def loginUsuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        usuario = authenticate(username=username, password=senha)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, "Logado com sucesso")
            return redirect('menu')
        else:
            messages.error(request, "Nome de usuário ou senha errado")    

    return render(request, 'login.html')


def menu(request):
    return render(request, 'menu.html')


def registroAvaliacao(request):
    if request.method == 'POST':
        form = RegistroAvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = RegistroAvaliacaoForm()

    return render(request, 'registroAvaliacao.html', {'form': form})