from django.forms import forms, fields
import django
import datetime

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

class CadastroAula(forms.Form):
    id_profissional = fields.IntegerField(label='Id do profissional')
    max_alunos = fields.IntegerField(label='Numero máximo de alunos')
    especialidade = fields.IntegerField(label='Id da Especialidade')
    data = fields.DateTimeField(label="Data no formato (AAAA-MM-DD hh:mm:ss): ")

class CadastroConsultaMedica(forms.Form):
    id_profissional = fields.IntegerField(label='Id do profissional')
    data = fields.DateTimeField(label="Data no formato (AAAA-MM-DD hh:mm:ss): ")




