from django.forms import forms, fields
import django

FAVORITE_COLORS_CHOICES = [
    ('consultar_anteriores', 'consultar servicos anteriores'),
    ('consultar_futuros', 'consultar servicos futuros'),
    ('consultar_todos', 'consultar servicos anteriores e futuros'),
]

class PesquisaServico(forms.Form):

    id_cliente = fields.IntegerField(label='Id do cliente')
    tempo_consulta = fields.MultipleChoiceField(
        required=False,
        widget=django.forms.RadioSelect,
        choices=FAVORITE_COLORS_CHOICES,
    )
