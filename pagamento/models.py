import django.db
from django.db import models
from datetime import datetime

from usuario.models import Cliente, Medico, Professor


class CartaoDeCredito(models.Model):
    numero = models.CharField(max_length=16)
    saldo = models.IntegerField(default=0)
    validade = models.IntegerField(default=0)
    cvv = models.CharField(max_length=3)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)


class Pagamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    valor = models.IntegerField(default=0)
    data = models.DateTimeField(default=datetime.now, blank=True)

