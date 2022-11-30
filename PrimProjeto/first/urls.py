from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('registro', views.registroUsuario, name='registro'),
    path('login', views.loginUsuario, name='login'),
    path('logout', views.logoutUsuario, name='logout'),
    path('perfilUsuario',views.perfilUsuario, name='perfilUsuario'),
    path('updateUsuario', views.updateUsuario, name='updateUsuario'),
    path('registroAvaliacao', views.registroAvaliacao, name='registroAvaliacao'),
    path('avaliacao/<int:pk>', views.avaliacao, name='avaliacao'),
    path('notificacoes', views.notificacoes, name='notificacoes'),
    path('notificacoesUsuario', views.notificacoesUsuario, name='notificacoesUsuario'),
    path('deletar', views.deletarPerfilUsuario, name='deletar'),
    path('encontro', views.encontrar, name='encontro'),
    path('chat/<int:pk>/', views.chat, name='chat'),
    path('chatRecebe/<int:pk>/', views.chatRecebe, name='chatRecebe'),
    path('disciplina/<int:pk>/', views.disciplina, name='disciplina'),
    path('materiais/<int:pk>/', views.materiais, name='materiais'),
]
