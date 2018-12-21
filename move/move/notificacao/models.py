from django.db import models

# Create your models here.
class Setor(models.Model):
    nome = models.CharField(max_length=60, null=False)
    esferaPublica = models.CharField(max_length=1, null=False,
                                     default='M')

class Usuario(models.Model):
    cpf = models.CharField(max_length=11, null=False)
    rg = models.CharField(max_length=10, null=False)
    nome = models.CharField(max_length=120, null=False)
    pai = models.CharField(max_length=120)
    mae = models.CharField(max_length=120, null=False)
    endereco = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=14)
    nickname = models.CharField(max_length=20, null=False)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

class Categoria(models.Model):
    nome = models.CharField(max_length=50, null=False)
    esferaPublica = models.CharField(max_length=1, null=False)

class Problema(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=80, null=False)

class Ocorrencia (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255, null=False)
    prazo = models.IntegerField(null=False)
    dataAbertura = models.DateTimeField(null=False)

class Mensagem (models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.TextField(null=False)

class Solucionador (models.Model):
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    ordem = models.IntegerField(null=False)
