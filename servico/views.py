import datetime
from copy import deepcopy
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Esse é o controller

from .models import *
from .forms import *


def index(request):
    return HttpResponse("Olá, Mundo!")


# verificar se cliente é válido
@csrf_exempt

def cadastrar_aula(request):
    id_profissional = request.GET['id_profissional']
    try:
        professor = Professor.objects.get(pk=id_profissional)
    except:
        raise HttpResponseBadRequest("Profissional não cadastrado no Sistema")

    especialidade_id = request.GET['especialidade']
    try:
        especialidade = Especialidade.objects.get(pk=especialidade_id)
    except:
        raise HttpResponseBadRequest("Especialidade não cadastrada no Sistema")

    max_alunos = int(request.GET['max_alunos'])
    if max_alunos < 0:
        raise HttpResponseBadRequest("Não é permitido quantidade negativa de alunos")

    data = request.GET['data']
    if datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S').timestamp() < datetime.datetime.now().timestamp():
        raise HttpResponse("Não é permitido cadastrar aula no Passado")
    try:
        nova_aula = Aula(data_hora=data, professor=professor, max_alunos=max_alunos, especialidade=especialidade)
        nova_aula.save()
        return HttpResponse("Aula criada com sucesso!")
    except:
        raise HttpResponseServerError("Erro na criação da aula")


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


def cadastrar_consulta_medica(request, medico_id, timestamp):
    try:
        medico = Medico.objects.get(pk=medico_id)
    except:
        raise HttpResponseBadRequest("Erro! Medico inválido")

    try:
        data_hora = datetime.fromtimestamp(timestamp)
    except:
        raise HttpResponseBadRequest("Erro! Data inválida - timespamp incorreto")

    if data_hora < datetime.now():
        raise HttpResponseBadRequest("Erro! Data inválida - data informada no passado")

    try:
        nova_consulta = Consulta(data_hora=data_hora, medico=medico)
        nova_consulta.save()
        return HttpResponse("Consulta Médica criada com sucesso!")
    except:
        raise HttpResponseServerError("Erro na criação da aula")


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
        raise HttpResponseBadRequest("Cliente não encontrado")

    try:
        if request.GET['tempo_consulta'] == 'consultar_anteriores':
            aulas = Aula.buscar_por_cliente(cliente, futuras=False)

        elif request.GET['tempo_consulta'] == 'consultar_futuras':
            aulas = Aula.buscar_por_cliente(cliente, passadas=False)

        else:  # opção consultar todos
            consultas = Consulta.buscar_por_cliente(cliente)
            aulas = Aula.buscar_por_cliente(cliente)

        context = {'lista_aulas': aulas}
        return render(request, 'aula/consultar.html', context)
    except:
        raise HttpResponseServerError("Erro")


def consultar_consulta_medica(request):
    cliente_id = request.GET['id_cliente']
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except:
        raise HttpResponseBadRequest("Cliente não encontrado")

    try:
        if request.GET['tempo_consulta'] == 'consultar_anteriores':
            consultas = Consulta.buscar_por_cliente(cliente, futuras=False)

        elif request.GET['tempo_consulta'] == 'consultar_futuras':
            consultas = Consulta.buscar_por_cliente(cliente, passadas=False)

        else:  # opção consultar todos
            consultas = Consulta.buscar_por_cliente(cliente)

        context = {'lista_consultas_medicas': consultas}

        return render(request, 'consulta_medica/consultar.html', context)
    except:
        raise HttpResponseServerError("Erro")


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
        raise HttpResponseBadRequest("Cliente não encontrado")

    try:
        if request.GET['tempo_consulta'] == 'consultar_anteriores':
            consultas = Consulta.buscar_por_cliente(cliente, futuras=False)
            aulas = Aula.buscar_por_cliente(cliente, futuras=False)

        elif request.GET['tempo_consulta'] == 'consultar_futuras':
            consultas = Consulta.buscar_por_cliente(cliente, passadas=False)
            aulas = Aula.buscar_por_cliente(cliente, passadas=False)

        else: # opção consultar todos
            consultas = Consulta.buscar_por_cliente(cliente)
            aulas = Aula.buscar_por_cliente(cliente)

        context = {'lista_consultas_medicas': consultas,
                   'lista_aulas': aulas}
        return render(request, 'geral/consultar.html', context)
    except:
        raise HttpResponseServerError("Erro")


def reservar_aula(request, cliente_id, aula_id):
    try:
        aluno = Cliente.objects.get(pk=cliente_id)
    except:
        raise HttpResponseForbidden('Erro! Cliente não encontrado')
    try:
        aula = Aula.objects.get(pk=aula_id)
    except:
        raise HttpResponseForbidden('Erro! Aula não encontrada')

    if aluno.status_assinatura != 'ativa':
        return HttpResponse(f'O aluno {aluno} não está com sua assinatura em dia. Cancelando operação.')

    if aula.alunos.filter(id__exact=cliente_id)[0].id == cliente_id:
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


def reservar_consulta_medica(request, cliente_id, consulta_medica_id):
    try:
        paciente = Cliente.objects.get(pk=cliente_id)
    except:
        raise HttpResponseForbidden('Erro! Cliente não encontrado')
    try:
        consulta_medica = Consulta.objects.get(pk=consulta_medica_id)
    except:
        raise HttpResponseForbidden('Erro! Consulta Médica não encontrada')

    if paciente.status_assinatura != 'ativa':
        return HttpResponse(f'O paciente {paciente} não está com sua assinatura em dia. Cancelando operação.')

    if consulta_medica.cliente is not None:
        return HttpResponse(f'Essa consulta já está reservada. Cancelando operação.')

    consulta_medica.cliente = paciente
    consulta_medica.save()
    return HttpResponse(
        f'Consulta Médica reservada!\n\tHorário: {consulta_medica.data_hora}\n\tMédico: {consulta_medica.medico}\n\tPaciente: {consulta_medica.cliente}')


def ordena_consultas(lista_strings):
    lista_strings_data = []
    for string in lista_strings:
        s = deepcopy(string)
        substring = s.split(";")
        dia_mes_ano = substring[1].split("/")
        hora_minuto = substring[2].split(":")
        dia = int(dia_mes_ano[0])
        mes = int(dia_mes_ano[1])
        ano = int(dia_mes_ano[2])
        hora = int(hora_minuto[0])
        minuto = int(hora_minuto[1])
        data_hora = datetime(ano, mes, dia, hora, minuto)
        par_string_data = (string, data_hora)
        lista_strings_data.append(par_string_data)
    lista_strings_data.sort(key=lambda i: i[1], reverse=True)
    nova_lista_strings = []
    for str in lista_strings_data:
        nova_lista_strings.append(str[0])
    return nova_lista_strings
