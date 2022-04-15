from django.db import models

from usuario.models import Cliente, Medico, Professor

class CartaoDeCredito(models.Model):
    numero = models.CharField(max_length=16)
    saldo = models.IntegerField(default=0)
    validade = models.DateTimeField()
    CVV = models.CharField(max_length=3)

    class Meta:
        abstract = True

class Pagamento(models.Model):
    cartao = models.ForeignKey(CartaoDeCredito, on_delete=models.CASCADE, null=True, blank=True)
    data_hora = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    valor = models.IntegerField(default=0)

    class Meta:
        abstract = True


