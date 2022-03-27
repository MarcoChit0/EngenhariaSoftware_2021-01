from django.db import models

# Create your models here.

class Especialidade(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


# MODELO DE USUÁRIO
class User(models.Model):
    name = models.CharField(max_length=50)  # Isso precisa virar chave primária? Não, chave primaria é o ID
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Cliente(User):
    client_desde = models.DateTimeField('Cliente desde')
    status_assinatura = 'ativa'
    payment_status = 'paid'  # 'not_paid'
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

# MODELOS DE SERVIÇOS
class Servico(models.Model):
    cliente = models.OneToOneField(Cliente, blank=True, null=True,
                                   default=None, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()

    class Meta:
        abstract = True


class Aula(Servico):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('professor', 'data_hora'))

    def __str__(self):
        prof = self.professor.name
        espec = self.especialidade.name
        dia = self.data_hora.day
        mes = self.data_hora.month
        hora = self.data_hora.hour
        minuto = self.data_hora.minute
        return f"{prof}, {espec}; {dia}/{mes} {hora}:{minuto}"


class Consulta(Servico):
    medico = models.OneToOneField(Medico, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('medico', 'data_hora'))
