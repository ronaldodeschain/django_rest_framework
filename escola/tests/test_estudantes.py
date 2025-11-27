from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin',
            email='email@email'
        )
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario) # type: ignore
        self.estudante_01 = Estudante.objects.create(
            nome = 'Teste Estudante UM',
            email = 'testeemailestudante01@gmail.com',
            cpf = '73231954037',
            data_nascimento = '2024-01-01',
            celular = '86 99999-9999',
        )
        self.estudante_02 = Estudante.objects.create(
            nome = 'Teste Estudante DOIS',
            email = 'testeemailestudante02@gmail.com',
            cpf = '76791271078',
            data_nascimento = '2024-01-01',
            celular = '86 99999-9999',
        )

    def test_requisicao_get_para_listar_estudantes(self):
        """Teste de requisição GET estudantes"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estudante(self):
        """Teste de requisição GET de um estudante"""
        url_detalhe = reverse('Estudantes-detail', kwargs={'pk': 1})
        response = self.client.get(url_detalhe)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(
            instance=dados_estudante).data
        self.assertEqual(response.data,dados_estudante_serializados) #type:ignore
    
    def test_requisicao_delete_um_estudante(self):
        """Teste de requisição DELETE um estudante"""
        response = self.client.delete(f'{self.url}2/')#/estudantes/2/
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
