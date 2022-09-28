from django.contrib import admin
from .models import usuario
from .models import disciplina
from .models import mensagem
from .models import avaliacao
from .models import pergunta
from .models import resposta
from .models import encontro
from .models import demanda


# Register your models here.

class usuario(models.Model):
    nome=models.CharField(max_length=30)
    sobrenome=models.CharField(max_length=30)
    email=models.EmailField()
    def _str_(self):
        return self.nome


class disciplina(models.Model):
    codigo=models.IntegerField(default=7)
    professores=models.TextField()
    materiais=models.TextField()

class mensagem(models.Model):
    data=models.DateField()
    hora=models.CharField(max_length=5)

class avaliacao(models.Model):
   professor=models.CharField(max_length=100)
   satisfacaoProfessor=models.CharField(max_length=7)
   cobranca=models.IntegerField(default=2) #pode ser 01,02..10
   horasFora=models.IntegerField()
   contribuicao=models.IntegerField(deffault=2)#mesma coisa da cobrança
   dificuldade=models.IntegerField(deffault=2)
   observacao=models.TextField()

class pergunta(models.Model):
    data=models.DateField()
    hora=models.CharField(max_length=5)
    conteudo=models.TextField()

class resposta(models.Model):
    data=models.DateField()
    hora=models.CharField(max_length=5)
    conteudo=models.TextField()

class encontro(models.Model):
    local=models.CharField(max_length=100)
    horaio=models.CharField(max_length=5)
    dia=models.DateField()
    pessoasConfirmadas=models.TextField()
    frequincia=models.CharField(max_length=100)

class demanda(models.Model):
    frequencia=models.CharField(max_length=100)

