from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome = forms.CharField(max_length=30)
    sobrenome = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username','nome', 'sobrenome', 'email', 'password1', 'password2')



