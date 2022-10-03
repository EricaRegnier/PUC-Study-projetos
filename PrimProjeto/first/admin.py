from django.contrib import admin
from .models import Usuario, Disciplina, Mensagem, Avaliacao, Pergunta, Resposta, Encontro, Demanda


# Register your models here.


admin.site.register(Usuario)
admin.site.register(Disciplina)
admin.site.register(Mensagem)
admin.site.register(Avaliacao)
admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(Encontro)
admin.site.register(Demanda)



"""
from first.models import Usuario
n=Usuario(nome=input("Digite seu primiro nome: "))
n.save()
s=Usuario(sobrenome=input("Digite seu sobrenome: "))
s.save()
e=Usuario(email=input("Digite seu e-mail: "))
e.save()

from first.models import Disciplina
c=Disciplina(codigo=input("Digite o codigo da dsiciplina: "))
c.save()
p=Disciplina(professores=input("Digite o nome dos professores: "))
p.save()
m=Disciplina(materiais=input("Materiais usados: "))
m.save()

from first.models import Mensagem
d=Mensagem(data=input("Data da mensagem: "))
d.save()
h=Mensagem(hora=input("hora da mensagem: "))
h.save()

from first.models import Avaliacao
p=Avaliacao(professor=input("Professor: "))
p.save()
s=Avaliacao(satisfacaoProfessor=input(" Numa escala de 0 a 10 qual foi a sua Satisfacao com o Professor? "))
s.save()
c=Avaliacao(cobranca=input("Numa escala de 0 a 10 qual o nivel de Cobranca da dsiciplina? "))
c.save()
h=Avaliacao(horasFora=input("Horas que voce passou estudando fora do horario de aula: "))
h.save()
cont=Avaliacao(contribuicao=input("Numa escala de 0 a 10,quanto a disciplina contribuiu para o seu progesso no curso? "))
cont.save()
d=Avaliacao(dificuldade=input("Numa escala de 0 a 10 qual e a dificuldade da disciplina: "))
d.save()
o=Avaliacao(observacao=input("Observacoes sobre a disciplina: "))
o.save()
from first.models import Pergunta
d=Pergunta(data=input("Data da pergunta: "))
d.save()
h=Pergunta(hora=input("Hora da pergunta: "))
h.save()
c=Pergunta(conteudo=input("Digite sua pergunta: "))
c.save()

from first.models import Resposta
d=Resposta(data=input("Data da resposta: "))
d.save()
h=Resposta(hora=input("Hora da resposta: "))
h.save()
c=Resposta(conteudo=input("Digite sua resposta: "))
c.save()

from first.models import Encontro
l=Encontro(local=input("Digite o local de encontro: "))
l.save()
h=Encontro(horario=input("Digite o horario de encontro: "))
h.save()
d=Encontro(dia=input("Digite o dia de encontro: "))
d.save()
p=Encontro(pessoasConfirmadas=input("Pessoas confirmadas no encontro: "))
p.save()
f=Encontro(frequincia=input("Digite a frequencia de encontro: "))
f.save()


from first.models import Demanda
f=Demanda(frequencia=input("Frequencia de atividades: "))
"""
