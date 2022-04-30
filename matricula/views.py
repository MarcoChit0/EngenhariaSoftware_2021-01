from django.shortcuts import render
from copy import deepcopy
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseServerError
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import CadastroForm
import pagamento
from usuario.models import Cliente

def realizar_matricula(request, cliente_id, cartao_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except:
        raise HttpResponseBadRequest("Erro! Cliente inválido")

    if cliente.payment_status == 'not_paid':
        # REALIZAR PAGAMENTO
        return redirect('http://127.0.0.1:8000/pagamento/realizar/'+ str(cliente_id) + '/20/' + str(cartao_id))


    elif cliente.payment_status == 'paid':
        return HttpResponseBadRequest("Cliente já está matriculado")
