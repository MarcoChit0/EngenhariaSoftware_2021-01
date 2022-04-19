from copy import deepcopy
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from json import *
from datetime import datetime
# Esse é o controller

from .models import *

def index(request):
    return HttpResponse("Olá, Mundo!")


# verificar se cliente é válido
@csrf_exempt
def cadastrar_aula(request, professor_id, especialidade_id, timestamp):
    try:
        professor = Professor.objects.get(pk=professor_id)
    except:
        raise HttpResponseBadRequest("Erro! Professor inválido")

    try:
        especialidade = Especialidade.objects.get(pk=especialidade_id)
    except:
        raise HttpResponseBadRequest("Erro! Especialidade inválida")
    
    try:
        data_hora=datetime.fromtimestamp(timestamp)
    except:
        raise HttpResponseBadRequest("Erro! Data inválida - timespamp incorreto")

    if data_hora < datetime.now():
        raise HttpResponseBadRequest("Erro! Data inválida - data informada no passado")
    
    try:
        nova_aula = Aula(data_hora= data_hora, professor=professor,especialidade=especialidade)
        nova_aula.save()
        return HttpResponse("Aula criada com sucesso!")
    except:
        raise HttpResponseServerError("Erro na criação da aula")

# verificar se cliente é válido
@csrf_exempt
def cadastrar_consulta_medica(request, medico_id, timestamp):
    try:
        medico = Medico.objects.get(pk=medico_id)
    except:
        raise HttpResponseBadRequest("Erro! Medico inválido")
    
    try:
        data_hora=datetime.fromtimestamp(timestamp)
    except:
        raise HttpResponseBadRequest("Erro! Data inválida - timespamp incorreto")
    
    if data_hora < datetime.now():
        raise HttpResponseBadRequest("Erro! Data inválida - data informada no passado")

    try:
        nova_consulta = Consulta(data_hora= data_hora, medico=medico)
        nova_consulta.save()
        return HttpResponse("Consulta Médica criada com sucesso!")
    except:
        raise HttpResponseServerError("Erro na criação da aula")

def consultar_aula(request, cliente_id):
    try:
        aulas = Aula.objects.filter(cliente_id=cliente_id).order_by('-data_hora')
        context = {'lista_aulas':aulas}
        return render(request, 'aula/consultar.html', context)
    except:
        raise HttpResponseServerError("Erro")

def consultar_consulta_medica(request, cliente_id):
    try:
        consultas = Consulta.objects.filter(cliente_id=cliente_id).order_by('-data_hora')
        context = {'lista_consultas_medicas':consultas}
        return render(request, 'consulta_medica/consultar.html', context)
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

    aula.alunos.add(aluno)
    aula.save()
    # Para garantir que o aluno ta ai
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
        data_hora = datetime(ano,mes,dia,hora,minuto)
        par_string_data = (string, data_hora)
        lista_strings_data.append(par_string_data)
    lista_strings_data.sort(key=lambda i:i[1], reverse=True)
    nova_lista_strings = []
    for str in lista_strings_data:
        nova_lista_strings.append(str[0])
    return nova_lista_strings
