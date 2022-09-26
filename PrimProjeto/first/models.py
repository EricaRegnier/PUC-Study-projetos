from django.db import models
from datetime import date

# Create your models here.

#tudo que tá vazio é pq eu não sei em qual classificação o atributo se encaixa

class usuario(models.Model):
    nome=models.CharField(max_length=30)
    sobrenome=models.CharField(max_length=30)
    email=models.EmailField()
    def _str_(self):
        return self.nome


class disciplina:
    codigo=models.IntegerField(default=7)
    professores=models.TextField()
    materiais=models.TextField()

class mensagem:
    data=models.DateField()
    hora=models.CharField(max_length=5)

class avaliacao:
   professor=models.CharField(max_length=100)
   satisfacaoProfessor=models.CharField(max_length=7)
   cobranca=models.IntegerField(default=2) #pode ser 01,02..10
   horasFora=models.IntegerField()
   contribuicao=models.IntegerField(deffault=2)#mesma coisa da cobrança
   dificuldade=models.IntegerField(deffault=2)
   observacao=models.TextField()

class pergunta:
    data=models.DateField()
    hora=models.CharField(max_length=5)
    conteudo=models.TextField()

class resposta:
    data=models.DateField()
    hora=models.CharField(max_length=5)
    conteudo=models.TextField()

class encontro:
    local=models.CharField(max_length=100)
    horaio=models.CharField(max_length=5)
    dia=models.DateField()
    pessoasConfirmadas=models.ManyToManyField()
    frequincia=models.CharField(max_length=100)

class demanda:
    frequencia=models.CharField(max_length=100)





