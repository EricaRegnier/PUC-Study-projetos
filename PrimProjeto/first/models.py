from django.db import models
from datetime import date

# Create your models here.


class Usuario(models.Model):
    nome=models.CharField(max_length=30)
    sobrenome=models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    codigo=models.IntegerField(default=7)
    professores=models.TextField()
    materiais=models.TextField()

class Mensagem(models.Model):
    data=models.DateField()
    hora=models.CharField(max_length=5)

class Avaliacao(models.Model):
   professor=models.CharField(max_length=100)
   satisfacaoProfessor=models.CharField(max_length=7)
   cobranca=models.IntegerField(default=2) #pode ser 01,02..10
   horasFora=models.IntegerField()
   contribuicao=models.IntegerField(default=2)#mesma coisa da cobrança
   dificuldade=models.IntegerField(default=2)
   observacao=models.TextField()

class Pergunta(models.Model):
    data=models.DateField()
    hora=models.CharField(max_length=5)
    conteudo=models.TextField()

class Resposta(models.Model):
    data=models.DateField()
    hora=models.CharField(max_length=5)
    conteudo=models.TextField()

class Encontro(models.Model):
    local=models.CharField(max_length=100)
    horaio=models.CharField(max_length=5)
    dia=models.DateField()
    pessoasConfirmadas=models.ManyToManyField(Usuario)
    frequincia=models.CharField(max_length=100)

class Demanda(models.Model):
    frequencia=models.CharField(max_length=100)





