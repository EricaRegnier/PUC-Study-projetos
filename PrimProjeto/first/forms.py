from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avaliacao


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome = forms.CharField(max_length=30)
    sobrenome = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username','nome', 'sobrenome', 'email', 'password1', 'password2')


class RegistroAvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ('professor','satisfacaoProfessor','cobranca','horasFora','contribuicao','dificuldade','observacao')
