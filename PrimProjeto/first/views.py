from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
from django.db.models import Avg
from django.http import JsonResponse
from .forms import RegistroForm, RegistroAvaliacaoForm, UpdateUsuarioForm, MarcarEncontroForm
from .models import Mensagem, Disciplina, Usuario, Conexao
from datetime import datetime, timedelta


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


def avaliacao(request, pk):
    disciplina = Disciplina.objects.get(id=pk)
    avaliacoes = disciplina.avaliacao_set.all()
    context= {
        'horas': avaliacoes.aggregate(mediaHoras=Avg('horasFora')),
        'cobranca': avaliacoes.aggregate(mediaCobranca=Avg('cobranca')),
        'disciplina': disciplina
    }
    return render(request, 'área_de_ver_avs.html', context)


def notificacoes(request):
    return render(request, 'notificacoes.html')
    
    
def notificacoesUsuario(request):
    usuario=request.user
    perguntas = usuario.pergunta_set.all()
    return render(request, 'Notificações do usuário.html', {'perguntas': perguntas})


def deletarPerfilUsuario(request):
    if request.method=='POST':
        email=request.POST['email']
        senha=request.POST['senha']
        usuario = authenticate(username=email, password=senha)
        if usuario is not None and usuario==request.user:
            usuario.delete()
            messages.success(request, "Perfil deletado com sucesso")
            return redirect('login')
        else:
            messages.error(request, "Nome de usuário ou senha errado")
      
    return render(request,'deletarPerfil.html')
   
def encontrar(request):
    if request.method=='POST':
        form=MarcarEncontroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MarcarEncontroForm()
    return render(request, 'encontros.html', {'form': form})   
    

def chat(request, pk):
    usuario = request.user
    disciplina = Disciplina.objects.get(id=pk)
    conexoes = disciplina.conexao_set.all()
    if not conexoes.filter(usuario=usuario):
        conexao = Conexao.objects.create(usuario=usuario, disciplina=disciplina)
        conexao.save()
    else:
        conexao = conexoes.get(usuario=usuario)
        conexao.ultAtivo = datetime.now()

    return render(request, 'chat.html', {'disciplina':disciplina})


def chatRecebe(request,pk):
    usuario = request.user
    disciplina = Disciplina.objects.get(id=pk)
    conexoes = disciplina.conexao_set.all()
    mensagens = disciplina.mensagem_set.all()
    usuarios = Usuario.objects.all()
    conexao = conexoes.get(usuario=usuario)
    conexao.ultAtivo = timezone.now()
    conexao.save()
    online = conexoes.filter(ultAtivo__gt = timezone.now()-timedelta(seconds=5))

    return JsonResponse({"mensagens":list(mensagens.values()), "usuarios":list(usuarios.values()), "usuario_id":request.user.id, "online":list(online.values())})


def chatEnvia(request):
    usuario = request.user
    texto = request.POST['texto']
    disciplina_id = request.POST['disciplina_id']
    print(disciplina_id)
    disciplina = Disciplina.objects.get(id=disciplina_id)
    mensagem = Mensagem.objects.create(usuario=usuario, texto=texto, disciplina=disciplina)
    mensagem.save()


def disciplina(request, pk):
    disciplina = Disciplina.objects.get(id=pk)
    return render(request, 'disciplina.html', {'disciplina':disciplina})


def materiais(request, pk):
    disciplina = Disciplina.objects.get(id=pk)
    materiais = disciplina.material_set.all()
    return render(request, 'materiais.html', {'disciplina':disciplina, 'materiais':materiais})