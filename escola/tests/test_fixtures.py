from django.test import TestCase

from escola.models import Estudante,Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixture(self):
        """Teste que verifica o carregamento da fixture"""
        estudante = Estudante.objects.get(cpf='57613856003')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular,'28 96124-9346')
        self.assertEqual(curso.codigo,'CPOO1')