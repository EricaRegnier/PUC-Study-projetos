from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, deletar
from .forms import RegistroForm, RegistroAvaliacaoForm, UpdateUsuarioForm


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
            return redirect('perfilUsuario')
        else:
            messages.error(request, "Nome de usuário ou senha errado")    

    return render(request, 'login.html')


def logoutUsuario(request):
    logout(request)
    return redirect('menu')


def perfilUsuario(request):
    usuario = request.user
    return render(request, 'perfilusuario.html', {'usuario':usuario})


def updateUsuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = UpdateUsuarioForm(request.POST, instance=usuario)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            form.save()
            return redirect('perfilUsuario')
    else:
        form = UpdateUsuarioForm(instance=usuario)

    return render(request, 'editarPerfil.html', {'form': form})


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


def notificacoes(request):
    return render(request, 'notificacoes.html')
    
    
def deletarPerfilUsuario(request):
    if request.method=='POST':
        email=request.POST['email']
        senha=request.POST['senha']
    usuario = authenticate(email=email, password=senha)
    if usuario is not None:
        deletar(request, usuario)
        messages.success(request, "Perfil deletado com sucesso")
        return redirect('login')
    else:
        messages.error(request, "Nome de usuário ou senha errado")
    
        
    return render(request,'deletarPerfil.html')
