from django.db import models

from especialidade.models import Especialidade

class User(models.Model):
    name = models.CharField(max_length=50)  # Isso precisa virar chave primária? Não, chave primaria é o ID
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Cliente(User):
    client_desde = models.DateTimeField('Cliente desde', auto_now_add=True)
    status_assinatura = 'ativa'
    payment_status = models.CharField(max_length=50, default='not_paid') # 'paid'
    payment_hist = []  # datas?
    next_trains = []  # datas?
    next_consultations = []  # datas?


class Profissional(User):
    class Meta:
        abstract = True


class Professor(Profissional):
    especialidades = models.ManyToManyField(Especialidade)


class Medico(Profissional):
    pass
