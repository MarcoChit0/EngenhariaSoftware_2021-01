from django.forms import forms, fields
import django

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

class CadastrarConsulta(forms.Form):
    id_medico = fields.IntegerField(label='Informe o Id do Médico:', required=True, )
    timestamp = fields.DateTimeField(label='Informe a data e horário da aula: (ex: 28/04/2022 14:00)',
                                     input_formats=['%d/%m/%Y %H:%M'],
                                     required=True,
                                     help_text='28/04/2022 14:00')

