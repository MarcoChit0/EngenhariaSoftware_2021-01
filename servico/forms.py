from select import select
from xmlrpc.client import DateTime
from django.forms import forms, fields
import django

from especialidade.models import Especialidade

from servico.models import Aula, Consulta, Servico
from usuario.models import Cliente

OPCOES_TEMPO = [
    ('consultar_anteriores', 'consultar servicos anteriores'),
    ('consultar_futuros', 'consultar servicos futuros'),
    ('consultar_todos', 'consultar servicos anteriores e futuros'),
]


class PesquisaServico(forms.Form):
    clientes = Cliente.objects.all()
    opcoes_clientes = []
    for c in clientes:
        opcoes_clientes.append((c.pk, c))
    id_cliente = fields.ChoiceField(label='Id do cliente', choices=opcoes_clientes)
    tempo_consulta = fields.MultipleChoiceField(
        required=True,
        widget=django.forms.RadioSelect,
        choices=OPCOES_TEMPO,
    )

class ContratarAulaForm(forms.Form):
    clientes = Cliente.objects.all()
    opcoes_clientes = []
    for c in clientes:
        opcoes_clientes.append((c.pk,c))
    id_cliente= fields.ChoiceField(label='Id do cliente',choices=opcoes_clientes)
    aulas = Aula.aulas_disponiveis()
    opcoes_aulas = []
    for a in aulas:
        opcoes_aulas.append((a.pk, a))
    id_aula= fields.ChoiceField(label='Id da aula',choices=opcoes_aulas)
class CadastrarConsulta(forms.Form):
    id_medico = fields.IntegerField(label='Informe o Id do Médico:', required=True, )
    timestamp = fields.DateTimeField(label='Informe a data e horário da aula: (ex: 28/04/2022 14:00)',
                                     input_formats=['%d/%m/%Y %H:%M'],
                                     required=True,
                                     help_text='28/04/2022 14:00')

class CadastroAula(forms.Form):
    especialidades = Especialidade.objects.all()
    choices = []
    for esp in especialidades:
        choices.append((esp.pk, esp))

    id_profissional = fields.IntegerField(label='Id do profissional')
    max_alunos = fields.IntegerField(label='Numero máximo de alunos')
    especialidade = fields.ChoiceField(label='Id da Especialidade',
                                       choices=choices)

    data = fields.DateTimeField(label="Data no formato (AAAA-MM-DD hh:mm:ss): ")


class CadastroConsultaMedica(forms.Form):
    id_profissional = fields.IntegerField(label='Id do profissional')
    data = fields.DateTimeField(label="Data no formato (AAAA-MM-DD hh:mm:ss): ")

class ContratarConsultaMedicaForm(forms.Form):
    clientes = Cliente.objects.all()
    opcoes_clientes = []
    for c in clientes:
        opcoes_clientes.append((c.pk,c))
    id_cliente= fields.ChoiceField(label='Id do cliente',choices=opcoes_clientes)
    consultas = Consulta.consultas_medicas_disponiveis()
    opcoes_consultas = []
    for c in consultas:
        opcoes_consultas.append((c.pk, c))
    id_consulta_medica = fields.ChoiceField(label='Id da consulta',choices=opcoes_consultas)