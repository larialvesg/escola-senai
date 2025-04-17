from django.db import models
from django.contrib.auth.models import User

class Patrimonio(models.Model):
    ni = models.CharField(max_length=20, unique=True)
    descricao = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)
    

class Ambiente(models.Model):
    sig = models.CharField(max_length=20, unique=True)
    descricao = models.CharField(max_length=100)
    sn = models.CharField(max_length=20, unique=True)
    responsavel = models.CharField(max_length=100)

class Gestor(models.Model):
    sn = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)


class Manutentor(models.Model):
    sn = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    area = models.CharField(max_length=50)
    gestor = models.ForeignKey(Gestor, on_delete=models.CASCADE)

class Area(models.Model):
    area = models.CharField(max_length=50)

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
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    manutentor = models.ForeignKey(Manutentor, on_delete=models.CASCADE, null=True, blank=True)
    prioridade = models.CharField(max_length=50, choices=prioridade_opcoes)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    sn = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return (
            f"Patrimônio: {self.patrimonio} | "
            f"Ambiente: {self.ambiente} | "
            f"Manutentor: {self.manutentor} | "
            f"Funcionário: {self.funcionario}"
            )
