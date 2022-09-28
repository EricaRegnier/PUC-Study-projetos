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

from first.models import usuario
n=usuario(nome=input("Digite seu primiro nome: "))
n.save()
s=usuario(sobrenome=input("Digite seu sobrenome: "))
s.save()
e=usuario(email=input("Digite seu e-mail: "))
e.save()

from first.models import disciplina
c=disciplina(codigo=input("Digite o codigo da dsiciplina: "))
c.save()
p=disciplina(professores=input("Digite o nome dos professores: "))
p.save()
m=disciplina(materiais=input("Materiais usados: "))
m.save()

from first.models import mensagem
d=mensagem(data=input("Data da mensagem: "))
d.save()
h=mensagem(hora=input("hora da mensagem: "))
h.save()

from first.models import avaliacao
p=avaliacao(professor=input("Professor: "))
p.save()
s=avaliacao(satisfacaoProfessor=input(" Numa escala de 0 a 7 qual foi a sua Satisfacao com o Professor? "))
s.save()
c=avaliacao(cobranca=input("Numa escala de 0 a 10 qual o nivel de Cobranca da dsiciplina? "))
c.save()
h=avaliacao(horasFora=input("Horas que voce passou estudando fora do horario de aula: "))
h.save()
cont=avaliacao(contribuicao=input("Numa escala de 0 a 10,quanto a disciplina contribuiu para o seu progesso no curso? "))
cont.save()
d=avaliacao(dificuldade=input("Numa escala de 0 a 10 qual e a dificuldade da disciplina: "))
d.save()
o=avaliacao(observacao=input("Observacoes sobre a disciplina: "))
o.save()
from first.models import pergunta
d=pergunta(data=input("Data da pergunta: "))
d.save()
h=pergunta(hora=input("Hora da pergunta: "))
h.save()
c=pergunta(conteudo=input("Digite sua pergunta: "))
c.save()

from first.models import resposta
d=resposta(data=input("Data da resposta: "))
d.save()
h=resposta(hora=input("Hora da resposta: "))
h.save()
c=resposta(conteudo=input("Digite sua resposta: "))
c.save()

from first.models import encontro
l=encontro(local=input("Digite o local de encontro: "))
l.save()
h=encontro(horario=input("Digite o horario de encontro: "))
h.save()
d=encontro(dia=input("Digite o dia de encontro: "))
d.save()
p=encontro(pessoasConfirmadas=input("Pessoas confirmadas no encontro: "))
p.save()
f=encontro(frequincia=input("Digite a frequencia de encontro: "))
f.save()


from first.models import demanda
f=demanda(frequencia=input("Frequencia de atividades: "))

