from django.shortcuts import render
from copy import deepcopy
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import CadastroForm

from usuario.models import Cliente


def realizar_matricula(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CadastroForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            data = form.cleaned_data
            print(data)

            name = data['name']
            password = data['password']
            numero = data['cartao_numero']
            validade = data['cartao_validade']
            cvv = data['cartao_cvv']
            saldo = 10 # valor da matricula?

            # TODO: adicionar user ao db
            user = Cliente(name=name, password=password)
            user.save()

            context = {'numero': numero, 'saldo': saldo, 'validade': validade, 'cvv': cvv, 'cliente_id': user.id}

            return render('cartao/cadastrar.html', context=context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CadastroForm()

    return render(request, 'realizar_matricula.html', {'form': form})