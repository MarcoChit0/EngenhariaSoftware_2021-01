from django.db import models
from especialidade.models import Especialidade

from usuario.models import Cliente, Medico, Professor

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
