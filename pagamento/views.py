from django.shortcuts import render
from copy import deepcopy
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from json import *

from .models import *


# verificar se cliente é válido

def index(request):
    return HttpResponse("Olá, Mundo!")

# é necessário saber o id de um cliente para realizar
@csrf_exempt
def cadastrar_cartao_de_credito(request, numero, saldo, validade, cvv, cliente_id):
    novo_cartao_de_credito = CartaoDeCredito(numero=numero, saldo=saldo, validade=validade, cvv=cvv, cliente_id=cliente_id)
    novo_cartao_de_credito.save()
    return HttpResponse("Cartao criado com sucesso")


@csrf_exempt
def realizar_pagamento(request, cliente_id, valor, cartao_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except:
        raise HttpResponseBadRequest("Erro! Cliente inválido")

    try:
        novo_pagamento = Pagamento(valor=valor, cliente_id=cliente_id)
        novo_pagamento.save()
        cliente.payment_status = 'paid'
        cliente.save()
        return HttpResponse("Pagamento realizado com sucesso")
    except:
        raise HttpResponseServerError("Erro na criação de cartao")
