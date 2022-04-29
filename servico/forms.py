from select import select
from xmlrpc.client import DateTime
from django.forms import forms, fields
import django

from servico.models import Aula, Consulta, Servico
from usuario.models import Cliente

OPCOES_TEMPO = [
    ('consultar_anteriores', 'consultar servicos anteriores'),
    ('consultar_futuros', 'consultar servicos futuros'),
    ('consultar_todos', 'consultar servicos anteriores e futuros'),
]

class PesquisaServico(forms.Form):
    id_cliente = fields.IntegerField(label='Id do cliente')
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
        print(c)
    id_consulta_medica = fields.ChoiceField(label='Id da consulta',choices=opcoes_consultas)