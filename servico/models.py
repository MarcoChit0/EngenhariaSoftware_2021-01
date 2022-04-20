from django.db import models
from django.db.models import CheckConstraint, Q

from especialidade.models import Especialidade

from usuario.models import Cliente, Medico, Professor

class Servico(models.Model):
    data_hora = models.DateTimeField()

    @staticmethod
    def buscar_por_cliente(cliente: Cliente):
        raise NotImplemented

    class Meta:
        abstract = True


class Aula(Servico):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    max_alunos = models.IntegerField()
    alunos = models.ManyToManyField(Cliente, blank=True, max_length=max_alunos)

    class Meta:
        unique_together = (('professor', 'data_hora'))

    # Query: buscar aulas ofertadas para um determinado id (passado e futuro)
    @staticmethod
    def buscar_por_cliente(cliente: Cliente):
        return Aula.objects.filter(alunos=cliente).order_by('-data_hora')


    def __str__(self):
        prof = self.professor.name
        espec = self.especialidade.name
        ano = self.data_hora.year
        dia = self.data_hora.day
        mes = self.data_hora.month
        hora = self.data_hora.hour
        minuto = self.data_hora.minute
        return f"{prof},{espec}; {dia}/{mes}/{ano}; {hora}:{minuto}"


class Consulta(Servico):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('medico', 'data_hora'))

    # Queries
    @staticmethod
    def buscar_por_cliente(cliente: Cliente):
        return Consulta.objects.filter(cliente=cliente).order_by('-data_hora')

    def __str__(self):
            med = self.medico.name
            dia = self.data_hora.day
            mes = self.data_hora.month
            hora = self.data_hora.hour
            minuto = self.data_hora.minute
            ano = self.data_hora.year
            return f"{med}; {dia}/{mes}/{ano}; {hora}:{minuto}"