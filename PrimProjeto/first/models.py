from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user=self.model(email=self.normalize_email(email), password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user=self.create_user(email, password=password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    nome=models.CharField(max_length=30)
    sobrenome=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin


class Disciplina(models.Model):
    codigo=models.CharField(max_length=7)
    professores=models.TextField()
    materiais=models.TextField()


class Mensagem(models.Model):
    data=models.DateField()
    hora=models.CharField(max_length=5)


class Avaliacao(models.Model):
   professor=models.CharField(max_length=100)
   satisfacaoProfessor=models.CharField(max_length=7)
   cobranca=models.IntegerField(default=2) #pode ser 01,02..10
   horasFora=models.IntegerField()
   contribuicao=models.IntegerField(default=2)#mesma coisa da cobrança
   dificuldade=models.IntegerField(default=2)
   observacao=models.TextField()


class Pergunta(models.Model):
    data=models.DateField()
    hora=models.TimeField()
    conteudo=models.TextField()
    usuario=models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    disciplina=models.ForeignKey(Disciplina, on_delete=models.RESTRICT)


class Resposta(models.Model):
    data=models.DateField()
    hora=models.TimeField()
    conteudo=models.TextField()
    usuario=models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    pergunta=models.ForeignKey(Pergunta, on_delete=models.RESTRICT)


class Encontro(models.Model):
    local=models.CharField(max_length=100)
    horario=models.TimeField()
    dia=models.DateField()
    pessoasConfirmadas=models.ManyToManyField(Usuario)
    frequencia=models.CharField(max_length=100)


class Demanda(models.Model):
    frequencia=models.CharField(max_length=100)