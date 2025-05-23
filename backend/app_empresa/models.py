from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
    area = models.CharField(max_length=50)

class Funcionario(models.Model):
    sn = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)

class Ambiente(models.Model):
    sig = models.CharField(max_length=20, unique=True)
    descricao = models.CharField(max_length=100)
    sn = models.CharField(max_length=20)
    responsavel = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True)

class Patrimonio(models.Model):
    ni = models.CharField(max_length=20, unique=True)
    descricao = models.CharField(max_length=100)
    localizacao = models.ForeignKey(Ambiente, on_delete=models.CASCADE, null=True, blank=True)

class OrdemDeServico(models.Model):
    descricao = models.CharField(max_length=100)
    abertura = models.DateField(auto_now_add=True)
    fechamento = models.DateTimeField(null=True, blank=True)
    status_opcoes = [
    ('iniciada', 'Iniciada'),
    ('pendente', 'Pendente'),
    ('finalizada', 'Finalizada'),
    ('cancelada', 'Cancelada'),]
    prioridade_opcoes = [
    ('alta', 'Alta'),
    ('media', 'Media'),
    ('baixa', 'Baixa'),]
    status = models.CharField(max_length=50, choices=status_opcoes)
    patrimonio = models.ForeignKey(Patrimonio, on_delete=models.CASCADE, null=True, blank=True)
    prioridade = models.CharField(max_length=50, choices=prioridade_opcoes)
    requisitante = models.ForeignKey(User, on_delete=models.CASCADE)
    manutentor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    sn = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return (
            f"Patrimônio: {self.patrimonio} | "
            f"Manutentor: {self.manutentor} | "
            f"Funcionário: {self.requisitante}"
            )
