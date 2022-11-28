import uuid

from django.db import models


class Status(models.TextChoices):
    SAIDA = "Saída"
    ENTRADA = "Entrada"
   


class Clientes(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tipo = models.CharField(max_length=98)
    data = models.CharField(max_length=25)
    natureza = models.CharField(max_length=98, choices=Status.choices)
    sinal = models.CharField(max_length=1)
    valor = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=25)
    dono_nome = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)
