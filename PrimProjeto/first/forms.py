from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Avaliacao,Usuario


class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'sobrenome', 'email', 'password1', 'password2')


class UpdateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'sobrenome', 'email')


class RegistroAvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ('professor','satisfacaoProfessor','cobranca','horasFora','contribuicao','dificuldade','observacao')
