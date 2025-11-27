from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import authenticate
from django.urls import reverse

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin',
            email='email@email'
        )
        self.url = reverse('Estudantes-list')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Test que verifica credenciais corretas do user"""
        usuario = authenticate(username='admin',password='admin')
        self.assertTrue((usuario is not None )and usuario.is_authenticated)
    
    def test_autenticacao_user_com_username_incorreto(self):
        """Test que verifica credenciais de username incorretos"""
        usuario = authenticate(username='admn',password='admin')
        self.assertFalse((usuario is not None )and usuario.is_authenticated)

    def test_autenticacao_user_com_password_incorreto(self):
        """Test que verifica credenciais de senha incorretas """
        usuario = authenticate(username='admin',password='admn')
        self.assertFalse((usuario is not None )and usuario.is_authenticated)

    def test_requisicao_get_autorizada(self):
        """Test que verifica uma requisição GET autorizada"""
        self.client.force_authenticate(user=self.usuario) # type: ignore 
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_get_nao_autorizada(self):
        """Test que verifica uma requisição GET não autorizada"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)