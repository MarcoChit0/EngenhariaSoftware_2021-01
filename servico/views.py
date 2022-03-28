from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from json import *
from datetime import datetime
# Esse é o controller

from .models import *

def index(request):
    return HttpResponse("Olá, Mundo!")

@csrf_exempt
def cadastrar_aula(request):
    # Verifica se o id é de professor, senão, não pode criar
    try:
        professor_id = int(request.GET.get("professor"))
        professor = Professor.objects.get(pk=professor_id)
    except:
        raise HttpResponseForbidden("Apenas professores podem criar aulas novas")

    try:
        # Pega infos do body da requisição
        # Considero um JSON com os elementos citados, se não tiver esses dados, erro
        infos = loads(request.body)
        timestamp = infos["timestamp"]
        especialidade_id = infos["especialidade_id"]
        especialidade = Especialidade.objects.get(pk=especialidade_id)
    except:
        raise HttpResponseBadRequest("Erro na requisição, verificar corpo da consulta")

    try:
        # Tenta criar nova aula, se der retorna, se não, erro do servidor
        nova_aula = Aula(data_hora=datetime.fromtimestamp(timestamp), professor=professor,
                         especialidade=especialidade)
        nova_aula.save()
        return HttpResponse("Success")
    except:
        raise HttpResponseServerError("Erro na criação da aula")


def consultar_aulas(request):  # TODO receber data? [filtros]
    response = ''
    # retornar lista com aulas cadastradas
    # e sem alunos inscritos
    aulas_disponiveis = Aula.objects.filter(cliente_id=None)

    # TODO transformar a response em algo estruturado (JSON/XML?)
    if len(aulas_disponiveis):
        response += f'Há {len(aulas_disponiveis)} aulas disponíveis no momento:\n\n'
        for aula in aulas_disponiveis:
            response += f'\tHorário: {aula.data_hora} - Professor: {aula.professor}\n'
    else:
        response = 'Não há aulas disponíveis no momento'

    return HttpResponse(response)


def reservar_aula(request):
    try:
        aluno_id = int(request.GET.get("aluno_id"))
        aula_id = int(request.GET.get("aula_id"))
        aluno = Cliente.objects.get(pk=aluno_id)
        aula = Aula.objects.get(pk=aula_id)
    except:
        raise HttpResponseForbidden('Aula e/ou aluno não encontrado. Cancelando operação.')

    # Checando possibilidade
    if aluno.status_assinatura != 'ativa':
        return HttpResponse(f'O aluno {aluno} não está com sua assinatura em dia. Cancelando operação.')
    if aula.cliente is not None:
        return HttpResponse(f'Esta aula já está reservada. Cancelando operação.')

    # Tudo ok
    aula.cliente = aluno
    aula.save()
    return HttpResponse(
        f'Aula reservada!\n\tHorário: {aula.data_hora}\n\tProfessor: {aula.professor}\n\tAluno: {aula.cliente}')

