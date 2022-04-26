import datetime
from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from especialidade.models import Especialidade
from servico.models import Consulta, Aula
from usuario.models import Cliente, Medico, Professor


class UtilsMocks:
    @staticmethod
    def mock_medico():
        medico = Medico(name='Hans Chucrute',
                        password='Pica-pau')
        medico.save()
        return medico

    @staticmethod
    def mock_consulta_sem_cliente():
        medico = UtilsMocks.mock_medico()
        consulta = Consulta(data_hora=(timezone.now() + datetime.timedelta(days=5)),
                            medico=medico)
        consulta.save()
        return consulta

    @staticmethod
    def mock_cliente():
        cliente = Cliente(name='Terry Crews',
                          password='Yogurt',
                          client_desde=timezone.now() - datetime.timedelta(days=20))
        cliente.save()
        return cliente

    @staticmethod
    def mock_especialidade():
        especialidade = Especialidade(name='levantamento de sacola')
        especialidade.save()
        return especialidade

    @staticmethod
    def mock_professor():
        professor = Professor(name='Johnny Bravo',
                              password='Johny Bravo')
        professor.save()
        return professor

    @staticmethod
    def mock_aula_sem_cliente():
        prof = UtilsMocks.mock_professor()
        espec = UtilsMocks.mock_especialidade()
        aula = Aula(data_hora=(timezone.now() + datetime.timedelta(days=5)),
                    professor=prof,
                    especialidade=espec,
                    max_alunos=1)
        aula.save()
        return aula


class ConsultaModelTest(TestCase):
    def teste_criar_consulta_sem_cliente(self):
        consulta = UtilsMocks.mock_consulta_sem_cliente()
        self.assertEqual(consulta.cliente, None)

    def teste_buscar_consulta_cliente(self):
        consulta = UtilsMocks.mock_consulta_sem_cliente()
        cliente = UtilsMocks.mock_cliente()
        consulta.cliente = cliente
        consulta.save()
        consultas_cliente = Consulta.buscar_por_cliente(cliente)
        self.assertTrue(consultas_cliente.contains(consulta))

    def teste_busca_consulta_cliente_sem_consulta(self):
        # Cria uma consulta pra outro cliente que não o que tem marcado
        consulta = UtilsMocks.mock_consulta_sem_cliente()
        cliente = UtilsMocks.mock_cliente()
        consulta.cliente = cliente
        consulta.save()
        outro_cliente = UtilsMocks.mock_cliente()
        consultas_outro_cliente = Consulta.buscar_por_cliente(outro_cliente)
        self.assertEqual(len(consultas_outro_cliente), 0)


class AulasModelTest(TestCase):
    def teste_criar_aula_sem_aluno(self):
        aula = UtilsMocks.mock_aula_sem_cliente()
        self.assertEqual(aula.alunos.count(), 0)

    def teste_adicionar_aluno_aula_com_vaga(self):
        aula = UtilsMocks.mock_aula_sem_cliente()
        aluno = UtilsMocks.mock_cliente()
        result = aula.add_aluno(aluno)
        aula.save()
        self.assertTrue(result)
        self.assertEqual(aula.alunos.count(), aula.max_alunos)

    def teste_adicionar_aluno_aula_cheia(self):
        aula = UtilsMocks.mock_aula_sem_cliente()
        # Aluno entra com sucesso
        aluno1 = UtilsMocks.mock_cliente()
        result1 = aula.add_aluno(aluno1)
        aula.save()
        self.assertTrue(result1)
        # Aluno não consegue entrar
        aluno2 = UtilsMocks.mock_cliente()
        result2 = aula.add_aluno(aluno2)
        aula.save()
        self.assertFalse(result2)
        # Apenas 1 aluno deve estar cadastrado na aula
        self.assertEqual(aula.alunos.count(), aula.max_alunos)

    def teste_buscar_aula_aluno(self):
        aula = UtilsMocks.mock_aula_sem_cliente()
        aluno = UtilsMocks.mock_cliente()
        aula.add_aluno(aluno)
        aula.save()
        aula_cliente = Aula.buscar_por_cliente(aluno)
        self.assertTrue(aula_cliente.contains(aula))

    def teste_buscar_aula_aluno_sem_aulas(self):
        aula = UtilsMocks.mock_aula_sem_cliente()
        aluno = UtilsMocks.mock_cliente()
        aula_cliente = Aula.buscar_por_cliente(aluno)
        self.assertEqual(len(aula_cliente), 0)