import datetime
from copy import deepcopy
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseRedirect, \
    HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Esse é o controller

from .models import *
from .forms import *


def index(request):
    return render(request, 'menu/index.html', {})


class Cadastrar:
    # verificar se cliente é válido
    @csrf_exempt
    def cadastrar_aula(request):
        id_profissional = request.GET['id_profissional']
        try:
            professor = Professor.objects.get(pk=id_profissional)
        except:
            return HttpResponseBadRequest("Profissional não cadastrado no Sistema")

        especialidade_id = request.GET['especialidade']
        try:
            especialidade = Especialidade.objects.get(pk=especialidade_id)
        except:
            return HttpResponseBadRequest("Especialidade não cadastrada no Sistema")

        max_alunos = int(request.GET['max_alunos'])
        if max_alunos < 0:
            return HttpResponseBadRequest("Não é permitido quantidade negativa de alunos")

        data = request.GET['data']
        if datetime.strptime(data, '%Y-%m-%d %H:%M:%S').timestamp() < datetime.now().timestamp():
            return HttpResponse("Não é permitido cadastrar aula no Passado")
        try:
            nova_aula = Aula(data_hora=data, professor=professor, max_alunos=max_alunos, especialidade=especialidade)
            nova_aula.save()
            return HttpResponse("Aula criada com sucesso!")
        except:
            return HttpResponseServerError("Erro na criação da aula")


    # verificar se cliente é válido
    @csrf_exempt
    def gerar_cadastro_aula(request):
        # Se entrar como GET, abre um formulário
        if request.method == 'GET':
            form = CadastroAula(request.GET)
            context = {'form': form}
            if form.is_valid():
                return HttpResponse('/Serviço cadastrado com sucesso./')

        # Se não, cria um formulário em branco
        else:
            form = CadastroAula()
            context = {'form': form}

        return render(request, 'forms/interface_cadastro_aula.html', context)


    def gerar_cadastro_consulta(request):
        # Se entrar como GET, abre um formulário
        if request.method == 'GET':
            form = CadastroConsultaMedica(request.GET)
            context = {'form': form}
            if form.is_valid():
                return HttpResponse('/Serviço cadastrado com sucesso./')

        # Se não, cria um formulário em branco
        else:
            form = CadastroConsultaMedica()
            context = {'form': form}

        return render(request, 'forms/interface_cadastro_consulta_medica.html', context)


    def cadastrar_consulta_medica(request):
        medico_id = request.GET['id_profissional']
        try:
            medico = Medico.objects.get(pk=request.GET['medico_id'])
        except:
            return HttpResponseBadRequest("Erro! Medico inválido")

        data = request.GET['data']

        if datetime.strptime(data, '%Y-%m-%d %H:%M:%S').timestamp() < datetime.now().timestamp():
            return HttpResponseBadRequest("Não é permitido cadastrar aula no Passado")

        try:
            nova_consulta = Consulta(data_hora=data, medico=medico)
            nova_consulta.save()
            return HttpResponse("Consulta Médica criada com sucesso!")
        except:
            return HttpResponseServerError("Erro na criação da aula")


class Consultar:
    def gerar_consulta_aula(request):
        # Se entrar como GET, abre um formulário
        if request.method == 'GET':
            form = PesquisaServico(request.GET)
            context = {'form': form}
            if form.is_valid():
                return HttpResponse('/Pesquisa feita/')

        # Se não, cria um formulário em branco
        else:
            form = PesquisaServico()
            context = {'form': form}

        return render(request, 'forms/interface_busca_aulas.html', context)

    def consultar_aula(request):
        cliente_id = request.GET['id_cliente']
        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except:
            return HttpResponseBadRequest("Cliente não encontrado")

        try:
            if request.GET['tempo_consulta'] == 'consultar_anteriores':
                aulas = Aula.buscar_por_cliente(cliente, futuras=False)

            elif request.GET['tempo_consulta'] == 'consultar_futuros':
                aulas = Aula.buscar_por_cliente(cliente, passadas=False)

            else:  # opção consultar todos
                consultas = Consulta.buscar_por_cliente(cliente)
                aulas = Aula.buscar_por_cliente(cliente)

            context = {'lista_aulas': aulas}
            return render(request, 'aula/consultar.html', context)
        except:
            return HttpResponseServerError("Erro")

    def gerar_consulta_consulta_medica(request):
        # Se entrar como GET, abre um formulário
        if request.method == 'GET':
            form = PesquisaServico(request.GET)
            context = {'form': form}
            if form.is_valid():
                return HttpResponse('/Pesquisa feita/')

            # Se não, cria um formulário em branco
            else:
                form = PesquisaServico()
                context = {'form': form}

            return render(request, 'forms/interface_busca_consulta_medica.html', context)

    def consultar_consulta_medica(request):
        cliente_id = request.GET['id_cliente']
        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except:
            return HttpResponseBadRequest("Cliente não encontrado")

        try:
            if request.GET['tempo_consulta'] == 'consultar_anteriores':
                consultas = Consulta.buscar_por_cliente(cliente, futuras=False)

            elif request.GET['tempo_consulta'] == 'consultar_futuros':
                consultas = Consulta.buscar_por_cliente(cliente, passadas=False)

            else:  # opção consultar todos
                consultas = Consulta.buscar_por_cliente(cliente)

            context = {'lista_consultas_medicas': consultas}

            return render(request, 'consulta_medica/consultar.html', context)
        except:
            return HttpResponseServerError("Erro")

    def gerar_consulta_todos(request):
        # Se entrar como GET, abre um formulário
        if request.method == 'GET':
            form = PesquisaServico(request.GET)
            context = {'form': form}
            if form.is_valid():
                return HttpResponse('/Pesquisa feita/')

        # Se não, cria um formulário em branco
        else:
            form = PesquisaServico()
            context = {'form': form}

        return render(request, 'forms/interface_busca_geral.html', context)

    def consultar_servicos(request):
        cliente_id = request.GET['id_cliente']
        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except:
            return HttpResponseBadRequest("Cliente não encontrado")

        try:
            if request.GET['tempo_consulta'] == 'consultar_anteriores':
                consultas = Consulta.buscar_por_cliente(cliente, futuras=False)
                aulas = Aula.buscar_por_cliente(cliente, futuras=False)

            elif request.GET['tempo_consulta'] == 'consultar_futuros':
                consultas = Consulta.buscar_por_cliente(cliente, passadas=False)
                aulas = Aula.buscar_por_cliente(cliente, passadas=False)

            else:  # opção consultar todos
                consultas = Consulta.buscar_por_cliente(cliente)
                aulas = Aula.buscar_por_cliente(cliente)

            context = {'lista_consultas_medicas': consultas,
                       'lista_aulas': aulas}
            return render(request, 'geral/consultar.html', context)
        except:
            return HttpResponseServerError("Erro")


class Reservar:
    def reservar_aula(request):
        cliente_id = int(request.POST['id_cliente'])
        aula_id = int(request.POST['id_aula'])
        try:
            aluno = Cliente.objects.get(pk=cliente_id)
        except:
            return HttpResponseForbidden('Erro! Cliente não encontrado')
        try:
            aula = Aula.objects.get(pk=aula_id)
        except:
            return HttpResponseForbidden('Erro! Aula não encontrada')

        if aluno.payment_status != 'paid':
            return HttpResponse(f'O aluno {aluno} não está com sua assinatura em dia. Cancelando operação.')

        if len(aula.alunos.filter(id__exact=cliente_id)) != 0:
            return HttpResponse(f'Você ja está nessa aula. Cancelando operação.')

        if aula.alunos.count() >= aula.max_alunos:
            return HttpResponse(f'Essa aula já está cheia. Cancelando operação.')

        success = aula.add_aluno(aluno)
        if not success:
            return HttpResponse(f'Essa aula já está cheia. Cancelando operação.')

        aula.save()
        # Para garantir que o aluno ta ai, pega o aluno do banco de dados
        saved_aluno = aula.alunos.filter(id__exact=cliente_id)[0]
        return HttpResponse(
            f'Aula reservada!\n\tHorário: {aula.data_hora}\n\tProfessor: {aula.professor}\n\tAluno: {saved_aluno}')

    def reservar_consulta_medica(request):
        cliente_id = int(request.POST['id_cliente'])
        consulta_medica_id = int(request.POST['id_consulta_medica'])
        try:
            paciente = Cliente.objects.get(pk=cliente_id)
        except:
            return HttpResponseForbidden('Erro! Cliente não encontrado')
        try:
            consulta_medica = Consulta.objects.get(pk=consulta_medica_id)
        except:
            return HttpResponseForbidden('Erro! Consulta Médica não encontrada')

        if paciente.status_assinatura != 'ativa':
            return HttpResponse(f'O paciente {paciente} não está com sua assinatura em dia. Cancelando operação.')

        if consulta_medica.cliente is not None:
            return HttpResponse(f'Essa consulta já está reservada. Cancelando operação.')

        consulta_medica.cliente = paciente
        consulta_medica.save()
        return HttpResponse(
            f'Consulta Médica reservada!\n\tHorário: {consulta_medica.data_hora}\n\tMédico: {consulta_medica.medico}\n\tPaciente: {consulta_medica.cliente}')

    def gerar_formulario_contratar_aula(request):
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = ContratarAulaForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = ContratarAulaForm()

        return render(request, 'contratar-servicos/contratar-servico.html', {'form': form})

    def gerar_formulario_contratar_consulta_medica(request):
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = ContratarConsultaMedicaForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = ContratarConsultaMedicaForm()

        return render(request, 'contratar-servicos/contratar-servico.html', {'form': form})
