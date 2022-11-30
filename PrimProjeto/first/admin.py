from django.contrib import admin
from .models import Usuario, Disciplina, Mensagem, Avaliacao, Pergunta, Resposta, Encontro, Demanda, Conexao, Material


# Register your models here.


admin.site.register(Usuario)
admin.site.register(Disciplina)
admin.site.register(Mensagem)
admin.site.register(Avaliacao)
admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(Encontro)
admin.site.register(Demanda)
admin.site.register(Conexao)
admin.site.register(Material)