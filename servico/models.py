from copy import deepcopy
from datetime import datetime

import django.db
from django.db import models

from especialidade.models import Especialidade

from usuario.models import Cliente, Medico, Professor


class Servico(models.Model):
    data_hora = models.DateTimeField()

    @staticmethod
    def buscar_por_cliente(cliente: Cliente, passadas=True, futuras=True):
        raise NotImplemented

    class Meta:
        abstract = True


# ATENÇÃO, USAR self.add_aluno ao inves de self.alunos.add, para garantir max_alunos
class Aula(Servico):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    max_alunos = models.IntegerField()
    alunos = models.ManyToManyField(Cliente, blank=True)

    class Meta:
        unique_together = (('professor', 'data_hora'))

    # Queries
    """ add_aluno: adiciona um aluno caso haja vagas
        Observação: 
        Não salva no banco de dados, a operação save() deve ser usada
        em sequência
        
        params:
        aluno: Cliente que será cadastrado caso exista vagas
        
        return:
        True  - caso operação seja bem suscedida
        False - caso não tenha sido possível adicionar o aluno
    """
    def add_aluno(self, aluno: Cliente):
        if self.alunos.count() < self.max_alunos:
            self.alunos.add(aluno)
            return True
        else:
            return False

    """ buscar_por_cliente: busca aulas de um determinado cliente

        params:
        cliente: Cliente que será buscado
        passadas=True: Busca consultas passadas
        futuras=True: Busca consultas futuras

        return:
        None  - caso operação seja bem suscedida
        Erro - caso não seja possível achar o cliente
    """
    @staticmethod
    def buscar_por_cliente(cliente: Cliente, passadas=True, futuras=True):
        if not futuras:
            return Aula.objects.filter(alunos=cliente, data_hora__lt=datetime.now()).order_by('-data_hora')
        elif not passadas:
            return Aula.objects.filter(alunos=cliente, data_hora__gt=datetime.now()).order_by('-data_hora')
        else:
            return Aula.objects.filter(alunos=cliente).order_by('-data_hora')
    
    def aulas_disponiveis():
        aulas =  Aula.objects.all()
        lista_par_aula_data = []
        for aula in aulas:
            if aula.alunos.count() < aula.max_alunos:
                s = deepcopy(str(aula))
                substring = s.split(";")
                dia_mes_ano = substring[1].split("/")
                hora_minuto = substring[2].split(":")
                dia = int(dia_mes_ano[0])
                mes = int(dia_mes_ano[1])
                ano = int(dia_mes_ano[2])
                hora = int(hora_minuto[0])
                minuto = int(hora_minuto[1])
                data_hora = datetime(ano, mes, dia, hora, minuto)
                par_aula_data = (aula, data_hora)
                lista_par_aula_data.append(par_aula_data)
        aulas_disponiveis = []
        for par in lista_par_aula_data:
            if(par[1] >= datetime.now()):
                aulas_disponiveis.append(par[0])
        return aulas_disponiveis

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
    """ buscar_por_cliente: busca consultas de um determinado cliente

        params:
        cliente: Cliente que será buscado
        passadas=True: Busca consultas passadas
        futuras=True: Busca consultas futuras

        return:
        None  - caso operação seja bem suscedida
        Erro - caso não seja possível achar o cliente
    """
    @staticmethod
    def buscar_por_cliente(cliente: Cliente, passadas=True, futuras=True):
        if not futuras:
            return Consulta.objects.filter(cliente=cliente, data_hora__lt=datetime.now()).order_by('-data_hora')
        elif not passadas:
            return Consulta.objects.filter(cliente=cliente, data_hora__gt=datetime.now()).order_by('-data_hora')
        else:
            return Consulta.objects.filter(cliente=cliente).order_by('-data_hora')

    def __str__(self):
            med = self.medico.name
            dia = self.data_hora.day
            mes = self.data_hora.month
            hora = self.data_hora.hour
            minuto = self.data_hora.minute
            ano = self.data_hora.year
            return f"{med}; {dia}/{mes}/{ano}; {hora}:{minuto}"

    def consultas_medicas_disponiveis():
        consultas =  Consulta.objects.all()
        lista_par_consulta_data = []
        for consulta in consultas:
            if consulta.cliente is None:
                s = deepcopy(str(consulta))
                substring = s.split(";")
                dia_mes_ano = substring[1].split("/")
                hora_minuto = substring[2].split(":")
                dia = int(dia_mes_ano[0])
                mes = int(dia_mes_ano[1])
                ano = int(dia_mes_ano[2])
                hora = int(hora_minuto[0])
                minuto = int(hora_minuto[1])
                data_hora = datetime(ano, mes, dia, hora, minuto)
                par_consulta_data = (consulta, data_hora)
                lista_par_consulta_data.append(par_consulta_data)
        consultas_disponiveis = []
        for par in lista_par_consulta_data:
            if(par[1] >= datetime.now()):
                consultas_disponiveis.append(par[0])
        return consultas_disponiveis