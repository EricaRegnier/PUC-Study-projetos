from django.db import models
from datetime import date

# Create your models here.

#tudo que tá vazio é pq eu não sei em qual classificação o atributo se encaixa

class Usuario(models.Model):
    nome=models.CharField(max_length=30)
    sobrenome=models.CharField(max_length=30)
    email=models.EmailField()
    def _str_(self):
        return self.nome


class Disciplina:
    codigo=models.IntegerField(default=7)
    professores=models.TextField()
    materiais=models.TextField()

class Mensagem:
    data=models.DateField()
    hora=models.CharField(max_length=5)

class Avaliacao:
   professor=models.CharField(max_length=100)
   satisfacaoProfessor=models.CharField(max_length=7)
   cobranca=models.IntegerField(default=2) #pode ser 01,02..10
   horasFora=models.IntegerField()
   contribuicao=models.IntegerField(deffault=2)#mesma coisa da cobrança
   dificuldade=models.IntegerField(deffault=2)
   observacao=models.TextField()

class Pergunta:
    data=models.DateField()
    hora=models.CharField(max_length=5)
    conteudo=models.TextField()

class Resposta:
    data=models.DateField()
    hora=models.CharField(max_length=5)
    conteudo=models.TextField()

class Encontro:
    local=models.CharField(max_length=100)
    horaio=models.CharField(max_length=5)
    dia=models.DateField()
    pessoasConfirmadas=models.ManyToManyField()
    frequincia=models.CharField(max_length=100)

class Demanda:
    frequencia=models.CharField(max_length=100)





