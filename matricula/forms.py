from django import forms

class CadastroForm(forms.Form):
    name = forms.CharField(label='Nome Completo', max_length=50)
    password = forms.CharField(label='Senha', max_length=35)

    cartao_numero = forms.IntegerField(label='Número do cartão de crédito')
    cartao_validade = forms.IntegerField(label='Validade do cartão de crédito')
    cartao_cvv = forms.IntegerField(label='CVV do cartão de crédito')

    #  numero, saldo, validade, cvv, cliente_id

