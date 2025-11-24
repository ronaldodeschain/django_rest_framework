from django.test import TestCase
from escola.models import Estudante,Matricula,Curso

class ModelEstudanteTestCase(TestCase):
    # def test_falha(self):
    #     self.fail('Teste falhou =(')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '194.865.200-54',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999'
        )
    
    def test_verifica_atributos_estudante(self):
        """Testa os atributos do modelo de estudante"""
        self.assertEqual(self.estudante.nome,'Teste de Modelo')
        self.assertEqual(self.estudante.email,'testedemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf,'194.865.200-54')
        self.assertEqual(self.estudante.data_nascimento,'2023-02-02')
        self.assertEqual(self.estudante.celular,'86 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'ABC',
            descricao = 'descricao de teste',
            nivel = 'B'
        )

    def test_verifica_atributos_curso(self):
        """Testa os atributos de curso"""
        self.assertEqual(self.curso.codigo,'ABC')
        self.assertEqual(self.curso.descricao,'descricao de teste')
        self.assertEqual(self.curso.nivel,'B')

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome= 'Teste Modelo Matricula',
            email= 'testemodelomatricula@gmail.com',
            cpf='91546870040',
            data_nascimento= '2003-02-02',
            celular='86 99999-9999',
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',descricao='curso teste matricula',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )
    def test_verificar_atributos_matricula(self):
        """verifica os atributos da matricula"""
        self.assertEqual(self.matricula.estudante.nome,'Teste Modelo Matricula')
        self.assertEqual(self.matricula.curso.descricao,"curso teste matricula")
        self.assertEqual(self.matricula.periodo,'M')