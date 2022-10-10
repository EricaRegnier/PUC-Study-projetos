from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registroUsuario, name='registro'),
    path('login',views.loginUsuario, name='login'),
]
