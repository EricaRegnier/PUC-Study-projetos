from django.db import models

# Create your models here.

class usuario(models.Model):
    nome=models.CharField(max_length=100)
    sobrenome=models.CharField(max_length=100)
    email=models.EmailField()
    def _str_(self):
        return self.nome
        

class disciplina:
    codigo=models.IntegerField(default=7)
    professores=models.TextField()
    materiais=models.TextField()

class mensagem:
    data=models.DateField()
    hora=

class avaliacao:
   professor=models.CharField(max_length=100)
   satisfacaoProfessor=models.IntegerField(default=2)
   cobranca=
   horasFora=models.IntegerField()
   contribuicao=
   dificuldade=
   observacao=

class pergunta:
    data=models.DateField()
    hora=
    conteudo=models.TextField()

class resposta:
    data=models.DateField()
    hora=
    conteudo=models.TextField()

class encontro:
    local=
    horaio=
    dia=models.DateField()
    pessoasConfirmadas=models.ManyToManyField()
    frequincia=

class demanda:
    frequencia=





